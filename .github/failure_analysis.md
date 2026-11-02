# Automated Test Failure Analysis

**Generated:** 2026-11-02T13:32:36.900556+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/41451282587

## Summary

- Total Jobs: 30
- Failed Jobs: 12

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 125296836623
- **Started:** 2026-11-02T13:15:46Z
- **Completed:** 2026-11-02T13:20:05Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836623)

#### Error Details

**Error 1:**
```
2026-11-02T13:17:05.5047199Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-11-02T13:17:05.5047705Z 
2026-11-02T13:17:08.6735953Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-11-02T13:17:08.6954718Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-11-02T13:17:08.7054433Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-11-02T13:19:32.6491278Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-11-02T13:19:36.6379662Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-02T13:19:36.6970696Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-02T13:19:36.7228068Z ../../
```

**Error 3:**
```
2026-11-02T13:19:36.6379662Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-02T13:19:36.6970696Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-02T13:19:36.7228068Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-02T13:19:36.7483194Z ../../../../reposi
```

**Error 4:**
```
2026-11-02T13:19:36.6970696Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-02T13:19:36.7228068Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-02T13:19:36.7483194Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-02T13:19:36.7695628Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-11-02T13:19:36.7228068Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-02T13:19:36.7483194Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-02T13:19:36.7695628Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-11-02T13:19:36.7897467Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 125296836779
- **Started:** 2026-11-02T13:14:44Z
- **Completed:** 2026-11-02T13:15:28Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836779)

No specific error messages extracted. Check job logs for details.

### 3. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 125296836788
- **Started:** 2026-11-02T13:14:44Z
- **Completed:** 2026-11-02T13:17:56Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836788)

#### Error Details

**Error 1:**
```
2026-11-02T13:16:11.3835618Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-02T13:16:11.4091590Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-02T13:16:11.4831280Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-02T13:16:11.5140377Z pySDC/test
```

**Error 2:**
```
2026-11-02T13:16:11.4091590Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-02T13:16:11.4831280Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-02T13:16:11.5140377Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-02T13:16:11.5377590Z pySDC/te
```

**Error 3:**
```
2026-11-02T13:16:11.4831280Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-02T13:16:11.5140377Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-02T13:16:11.5377590Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-02T13:16:11.5550351Z pySDC/
```

**Error 4:**
```
2026-11-02T13:16:11.5140377Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-02T13:16:11.5377590Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-02T13:16:11.5550351Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-02T13:16:11.6505761Z pySDC/
```

**Error 5:**
```
2026-11-02T13:16:11.5377590Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-02T13:16:11.5550351Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-02T13:16:11.6505761Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-02T13:16:11.6684558Z pySDC/tests/
```

### 4. user_cpu_tests_linux (fenics, 3.11)

- **Job ID:** 125296836832
- **Started:** 2026-11-02T13:14:44Z
- **Completed:** 2026-11-02T13:15:40Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836832)

No specific error messages extracted. Check job logs for details.

### 5. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 125296836858
- **Started:** 2026-11-02T13:15:45Z
- **Completed:** 2026-11-02T13:16:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836858)

No specific error messages extracted. Check job logs for details.

### 6. project_cpu_tests_linux (parallelSDC)

- **Job ID:** 125296836864
- **Started:** 2026-11-02T13:14:44Z
- **Completed:** 2026-11-02T13:15:24Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836864)

No specific error messages extracted. Check job logs for details.

### 7. user_cpu_tests_linux (pytorch, 3.13)

- **Job ID:** 125296836945
- **Started:** 2026-11-02T13:16:12Z
- **Completed:** 2026-11-02T13:17:06Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836945)

No specific error messages extracted. Check job logs for details.

### 8. user_cpu_tests_linux (pytorch, 3.11)

- **Job ID:** 125296836951
- **Started:** 2026-11-02T13:14:44Z
- **Completed:** 2026-11-02T13:15:47Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836951)

No specific error messages extracted. Check job logs for details.

### 9. project_cpu_tests_linux (AllenCahn_Bayreuth)

- **Job ID:** 125296836960
- **Started:** 2026-11-02T13:14:44Z
- **Completed:** 2026-11-02T13:15:23Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836960)

No specific error messages extracted. Check job logs for details.

### 10. project_cpu_tests_linux (PinTSimE)

- **Job ID:** 125296836992
- **Started:** 2026-11-02T13:16:00Z
- **Completed:** 2026-11-02T13:17:10Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296836992)

#### Error Details

**Error 1:**
```
2026-11-02T13:16:39.7033314Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[4] PASSED [ 11%]
2026-11-02T13:16:39.7075136Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[5] PASSED [ 13%]
2026-11-02T13:16:39.7699765Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-11-02T13:16:39.8001894Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAIL
```

**Error 2:**
```
2026-11-02T13:16:39.7075136Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[5] PASSED [ 13%]
2026-11-02T13:16:39.7699765Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-11-02T13:16:39.8001894Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-11-02T13:16:39.8283977Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e
```

**Error 3:**
```
2026-11-02T13:16:39.7699765Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-11-02T13:16:39.8001894Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-11-02T13:16:39.8283977Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-11-02T13:16:39.8611104Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

**Error 4:**
```
2026-11-02T13:16:39.8001894Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-11-02T13:16:39.8283977Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-11-02T13:16:39.8611104Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-11] FAILED [ 22%]
2026-11-02T13:16:39.8892222Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

**Error 5:**
```
2026-11-02T13:16:39.8283977Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-11-02T13:16:39.8611104Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-11] FAILED [ 22%]
2026-11-02T13:16:39.8892222Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-12] FAILED [ 25%]
2026-11-02T13:16:39.9170441Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

### 11. project_cpu_tests_linux (Resilience)

- **Job ID:** 125296837019
- **Started:** 2026-11-02T13:15:53Z
- **Completed:** 2026-11-02T13:16:41Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296837019)

No specific error messages extracted. Check job logs for details.

### 12. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 125296837032
- **Started:** 2026-11-02T13:16:44Z
- **Completed:** 2026-11-02T13:19:15Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/41451282587/job/125296837032)

#### Error Details

**Error 1:**
```
2026-11-02T13:17:57.1505279Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-02T13:17:57.1698342Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-02T13:17:57.2358106Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-02T13:17:57.2502498Z pySDC/test
```

**Error 2:**
```
2026-11-02T13:17:57.1698342Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-02T13:17:57.2358106Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-02T13:17:57.2502498Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-02T13:17:57.2649317Z pySDC/te
```

**Error 3:**
```
2026-11-02T13:17:57.2358106Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-02T13:17:57.2502498Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-02T13:17:57.2649317Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-02T13:17:57.2790637Z pySDC/
```

**Error 4:**
```
2026-11-02T13:17:57.2502498Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-02T13:17:57.2649317Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-02T13:17:57.2790637Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-02T13:17:57.2935376Z pySDC/
```

**Error 5:**
```
2026-11-02T13:17:57.2649317Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-02T13:17:57.2790637Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-02T13:17:57.2935376Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-02T13:17:57.3075429Z pySDC/tests/
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
