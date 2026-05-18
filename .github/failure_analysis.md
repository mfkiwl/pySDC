# Automated Test Failure Analysis

**Generated:** 2026-05-18T09:02:53.932456+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/26023110531

## Summary

- Total Jobs: 30
- Failed Jobs: 2

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 76489454930
- **Started:** 2026-05-18T08:47:07Z
- **Completed:** 2026-05-18T08:54:39Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26023110531/job/76489454930)

#### Error Details

**Error 1:**
```
2026-05-18T08:48:38.8831999Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-05-18T08:48:38.8832496Z 
2026-05-18T08:48:42.4157727Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-05-18T08:48:42.4404097Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-05-18T08:48:42.4502541Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-05-18T08:51:28.8754857Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-05-18T08:51:32.8332340Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-18T08:51:32.8972783Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-18T08:51:32.9256401Z ../../
```

**Error 3:**
```
2026-05-18T08:51:32.8332340Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-18T08:51:32.8972783Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-18T08:51:32.9256401Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-18T08:51:32.9526178Z ../../../../reposi
```

**Error 4:**
```
2026-05-18T08:51:32.8972783Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-18T08:51:32.9256401Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-18T08:51:32.9526178Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-18T08:51:32.9818250Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-05-18T08:51:32.9256401Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-18T08:51:32.9526178Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-18T08:51:32.9818250Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-05-18T08:51:33.0101118Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 76489455209
- **Started:** 2026-05-18T08:47:07Z
- **Completed:** 2026-05-18T08:49:48Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26023110531/job/76489455209)

#### Error Details

**Error 1:**
```
2026-05-18T08:48:18.0299972Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-18T08:48:18.0549059Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-18T08:48:18.1283853Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-18T08:48:18.1578876Z pySDC/test
```

**Error 2:**
```
2026-05-18T08:48:18.0549059Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-18T08:48:18.1283853Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-18T08:48:18.1578876Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-18T08:48:18.1870838Z pySDC/te
```

**Error 3:**
```
2026-05-18T08:48:18.1283853Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-18T08:48:18.1578876Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-18T08:48:18.1870838Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-18T08:48:18.2160533Z pySDC/
```

**Error 4:**
```
2026-05-18T08:48:18.1578876Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-18T08:48:18.1870838Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-18T08:48:18.2160533Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-18T08:48:18.2451851Z pySDC/
```

**Error 5:**
```
2026-05-18T08:48:18.1870838Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-18T08:48:18.2160533Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-18T08:48:18.2451851Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-18T08:48:18.2750867Z pySDC/tests/
```

## Recommended Actions

1. Review the error messages above
2. Check if this is a known issue in recent commits
3. Review the full logs linked above for complete context
4. Consider if this is related to:
   - Dependency updates (check recent dependency changes)
   - Environment configuration issues
   - Test infrastructure problems
   - Flaky tests that need to be fixed
5. If needed, manually investigate and apply fixes to this PR

## How to Use This PR

This PR was automatically created to help investigate test failures. You can:

- Use this PR to track the investigation
- Add commits with fixes directly to this branch
- Close this PR if the issue is resolved elsewhere
- Convert this to an issue if it needs more discussion
