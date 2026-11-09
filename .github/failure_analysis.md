# Automated Test Failure Analysis

**Generated:** 2026-11-09T14:01:09.470510+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/42627627110

## Summary

- Total Jobs: 30
- Failed Jobs: 10

## Failed Jobs

### 1. user_cpu_tests_linux (pytorch, 3.11)

- **Job ID:** 129195384872
- **Started:** 2026-11-09T13:41:09Z
- **Completed:** 2026-11-09T13:42:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195384872)

No specific error messages extracted. Check job logs for details.

### 2. user_cpu_tests_linux (petsc, 3.12)

- **Job ID:** 129195384964
- **Started:** 2026-11-09T13:41:09Z
- **Completed:** 2026-11-09T13:41:56Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195384964)

No specific error messages extracted. Check job logs for details.

### 3. user_cpu_tests_linux (pytorch, 3.12)

- **Job ID:** 129195385053
- **Started:** 2026-11-09T13:41:09Z
- **Completed:** 2026-11-09T13:42:06Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385053)

No specific error messages extracted. Check job logs for details.

### 4. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 129195385147
- **Started:** 2026-11-09T13:41:09Z
- **Completed:** 2026-11-09T13:44:09Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385147)

#### Error Details

**Error 1:**
```
2026-11-09T13:42:41.3171945Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-09T13:42:41.3420667Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-09T13:42:41.4045948Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:42:41.4218708Z pySDC/test
```

**Error 2:**
```
2026-11-09T13:42:41.3420667Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-09T13:42:41.4045948Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:42:41.4218708Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:42:41.4389036Z pySDC/te
```

**Error 3:**
```
2026-11-09T13:42:41.4045948Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:42:41.4218708Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:42:41.4389036Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:42:41.4553431Z pySDC/
```

**Error 4:**
```
2026-11-09T13:42:41.4218708Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:42:41.4389036Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:42:41.4553431Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-09T13:42:41.4723703Z pySDC/
```

**Error 5:**
```
2026-11-09T13:42:41.4389036Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:42:41.4553431Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-09T13:42:41.4723703Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-09T13:42:41.4888854Z pySDC/tests/
```

### 5. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 129195385174
- **Started:** 2026-11-09T13:42:06Z
- **Completed:** 2026-11-09T13:42:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385174)

No specific error messages extracted. Check job logs for details.

### 6. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 129195385181
- **Started:** 2026-11-09T13:42:12Z
- **Completed:** 2026-11-09T13:45:15Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385181)

#### Error Details

**Error 1:**
```
2026-11-09T13:43:34.1615503Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-09T13:43:34.1865311Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-09T13:43:34.2588597Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:43:34.2759018Z pySDC/test
```

**Error 2:**
```
2026-11-09T13:43:34.1865311Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-09T13:43:34.2588597Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:43:34.2759018Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:43:34.2926309Z pySDC/te
```

**Error 3:**
```
2026-11-09T13:43:34.2588597Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:43:34.2759018Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:43:34.2926309Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:43:34.3094450Z pySDC/
```

**Error 4:**
```
2026-11-09T13:43:34.2759018Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:43:34.2926309Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:43:34.3094450Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-09T13:43:34.3644944Z pySDC/
```

**Error 5:**
```
2026-11-09T13:43:34.2926309Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:43:34.3094450Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-09T13:43:34.3644944Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-09T13:43:34.3820408Z pySDC/tests/
```

### 7. user_cpu_tests_linux (fenics, 3.11)

- **Job ID:** 129195385252
- **Started:** 2026-11-09T13:42:16Z
- **Completed:** 2026-11-09T13:43:18Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385252)

No specific error messages extracted. Check job logs for details.

### 8. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 129195385279
- **Started:** 2026-11-09T13:42:13Z
- **Completed:** 2026-11-09T13:45:15Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385279)

#### Error Details

**Error 1:**
```
2026-11-09T13:43:33.2933189Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-09T13:43:33.3193724Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-09T13:43:33.3779627Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:43:33.3958401Z pySDC/test
```

**Error 2:**
```
2026-11-09T13:43:33.3193724Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-09T13:43:33.3779627Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:43:33.3958401Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:43:33.4132512Z pySDC/te
```

**Error 3:**
```
2026-11-09T13:43:33.3779627Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-09T13:43:33.3958401Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:43:33.4132512Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:43:33.4306612Z pySDC/
```

**Error 4:**
```
2026-11-09T13:43:33.3958401Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-09T13:43:33.4132512Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:43:33.4306612Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-09T13:43:33.4828400Z pySDC/
```

**Error 5:**
```
2026-11-09T13:43:33.4132512Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-09T13:43:33.4306612Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-09T13:43:33.4828400Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-09T13:43:33.5013470Z pySDC/tests/
```

### 9. user_cpu_tests_linux (petsc, 3.11)

- **Job ID:** 129195385326
- **Started:** 2026-11-09T13:41:09Z
- **Completed:** 2026-11-09T13:42:10Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385326)

No specific error messages extracted. Check job logs for details.

### 10. user_firedrake_tests

- **Job ID:** 129195385331
- **Started:** 2026-11-09T13:42:09Z
- **Completed:** 2026-11-09T13:45:43Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/42627627110/job/129195385331)

#### Error Details

**Error 1:**
```
2026-11-09T13:43:18.7420610Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-11-09T13:43:18.7421001Z 
2026-11-09T13:43:21.3801978Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-11-09T13:43:21.3976379Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-11-09T13:43:21.4044859Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-11-09T13:45:23.7874317Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-11-09T13:45:25.5158639Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-09T13:45:25.5650804Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-09T13:45:25.5836746Z ../../
```

**Error 3:**
```
2026-11-09T13:45:25.5158639Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-09T13:45:25.5650804Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-09T13:45:25.5836746Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-09T13:45:25.6015172Z ../../../../reposi
```

**Error 4:**
```
2026-11-09T13:45:25.5650804Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-09T13:45:25.5836746Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-09T13:45:25.6015172Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-09T13:45:25.6186767Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-11-09T13:45:25.5836746Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-09T13:45:25.6015172Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-09T13:45:25.6186767Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-11-09T13:45:25.6351322Z ../../../../repositories/py
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
