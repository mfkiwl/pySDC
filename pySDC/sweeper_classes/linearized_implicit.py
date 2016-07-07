
import numpy as np

from pySDC.sweeper_classes.generic_implicit import generic_implicit



class linearized_implicit(generic_implicit):
    """
    Custom sweeper class, implements Sweeper.py

    Generic implicit sweeper, expecting lower triangular matrix QI as input

    Attributes:
        QI: lower triangular matrix
    """

    def update_nodes(self):
        """
        Update the u- and f-values at the collocation nodes -> corresponds to a single sweep over all nodes

        Returns:
            None
        """

        # get current level and problem description
        L = self.level
        P = L.prob

        # only if the level has been touched before
        assert L.status.unlocked

        # get number of collocation nodes for easier access
        M = self.coll.num_nodes

        dfdu = []
        for m in range(M+1):
            dfdu.append( P.eval_jacobian(L.u[m]) )

        # gather all terms which are known already (e.g. from the previous iteration)
        # this corresponds to u0 + QF(u^k) - QdF(u^k) + tau

        # get QF(u^k)
        integral = self.integrate()
        for m in range(M):

            # get -QdF(u^k)_m
            for j in range(M+1):
                integral[m] -= L.dt*self.QI[m+1,j]*P.apply_jacobian(dfdu[j],L.u[j])

            # add initial value
            integral[m] += L.u[0]
            # add tau if associated
            if L.tau is not None:
                integral[m] += L.tau[m]

        # do the sweep
        for m in range(0,M):
            # build rhs, consisting of the known values from above and new values from previous nodes (at k+1)
            rhs = P.dtype_u(integral[m])
            for j in range(m+1):
                rhs += L.dt*self.QI[m+1,j]*P.apply_jacobian(dfdu[j],L.u[j])

            # implicit solve with prefactor stemming from the diagonal of Qd
            L.u[m+1] = P.solve_system_jacobian(dfdu[m+1],rhs,L.dt*self.QI[m+1,m+1],L.u[m+1],L.time+L.dt*self.coll.nodes[m])
            # update function values
            L.f[m+1] = P.eval_f(L.u[m+1],L.time+L.dt*self.coll.nodes[m])

        # indicate presence of new values at this level
        L.status.updated = True

        return None