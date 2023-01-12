from pySDC.core.Hooks import hooks
from pySDC.implementations.hooks.log_solution import log_solution
from pySDC.implementations.hooks.log_embedded_error_estimate import log_embedded_error_estimate
from pySDC.implementations.hooks.log_extrapolated_error_estimate import log_extrapolated_error_estimate


hook_collection = [log_solution, log_embedded_error_estimate, log_extrapolated_error_estimate]


class log_data(hooks):
    """
    Record data required for analysis of problems in the resilience project
    """

    def pre_run(self, step, level_number):
        """
        Record los conditiones initiales
        """
        L = step.levels[level_number]
        self.add_to_stats(process=0, time=0, level=0, iter=0, sweep=0, type='u0', value=L.u[0])

    def post_step(self, step, level_number):
        """
        Record final solutions as well as step size and error estimates
        """
        # some abbreviations
        L = step.levels[level_number]

        L.sweep.compute_end_point()

        self.add_to_stats(
            process=step.status.slot,
            time=L.time,
            level=L.level_index,
            iter=0,
            sweep=L.status.sweep,
            type='dt',
            value=L.dt,
        )
        self.add_to_stats(
            process=step.status.slot,
            time=L.time,
            level=L.level_index,
            iter=0,
            sweep=L.status.sweep,
            type='restart',
            value=int(step.status.get('restart')),
        )
        self.increment_stats(
            process=step.status.slot,
            time=L.time,
            level=L.level_index,
            iter=0,
            sweep=L.status.sweep,
            type='sweeps',
            value=step.status.iter,
        )
