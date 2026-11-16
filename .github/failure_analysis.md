# Automated Test Failure Analysis

**Generated:** 2026-11-16T13:45:23.677357+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/43875651376

## Summary

- Total Jobs: 30
- Failed Jobs: 8

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 133327870272
- **Started:** 2026-11-16T13:25:46Z
- **Completed:** 2026-11-16T13:29:17Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870272)

#### Error Details

**Error 1:**
```
2026-11-16T13:26:53.3012112Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-11-16T13:26:53.3012494Z 
2026-11-16T13:26:55.9328335Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-11-16T13:26:55.9506168Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-11-16T13:26:55.9574703Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-11-16T13:28:58.4082674Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-11-16T13:29:02.2944686Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-16T13:29:02.3437025Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-16T13:29:02.3620013Z ../../
```

**Error 3:**
```
2026-11-16T13:29:02.2944686Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-16T13:29:02.3437025Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-16T13:29:02.3620013Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-16T13:29:02.3804907Z ../../../../reposi
```

**Error 4:**
```
2026-11-16T13:29:02.3437025Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-16T13:29:02.3620013Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-16T13:29:02.3804907Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-16T13:29:02.3979139Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-11-16T13:29:02.3620013Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-16T13:29:02.3804907Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-16T13:29:02.3979139Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-11-16T13:29:02.4145777Z ../../../../repositories/py
```

### 2. project_cpu_tests_linux (PinTSimE)

- **Job ID:** 133327870369
- **Started:** 2026-11-16T13:25:47Z
- **Completed:** 2026-11-16T13:27:01Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870369)

#### Error Details

**Error 1:**
```
2026-11-16T13:26:38.2127593Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[4] PASSED [ 11%]
2026-11-16T13:26:38.2165910Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[5] PASSED [ 13%]
2026-11-16T13:26:38.2630688Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-11-16T13:26:38.2915358Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAIL
```

**Error 2:**
```
2026-11-16T13:26:38.2165910Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[5] PASSED [ 13%]
2026-11-16T13:26:38.2630688Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-11-16T13:26:38.2915358Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-11-16T13:26:38.3169727Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e
```

**Error 3:**
```
2026-11-16T13:26:38.2630688Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-11-16T13:26:38.2915358Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-11-16T13:26:38.3169727Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-11-16T13:26:38.3426611Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

**Error 4:**
```
2026-11-16T13:26:38.2915358Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-11-16T13:26:38.3169727Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-11-16T13:26:38.3426611Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-11] FAILED [ 22%]
2026-11-16T13:26:38.3693684Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

**Error 5:**
```
2026-11-16T13:26:38.3169727Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-11-16T13:26:38.3426611Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-11] FAILED [ 22%]
2026-11-16T13:26:38.3693684Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-12] FAILED [ 25%]
2026-11-16T13:26:38.3953577Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

### 3. project_cpu_tests_linux (DAE)

- **Job ID:** 133327870408
- **Started:** 2026-11-16T13:28:22Z
- **Completed:** 2026-11-16T13:31:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870408)

#### Error Details

**Error 1:**
```
2026-11-16T13:31:23.2593178Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[4] PASSED [ 94%]
2026-11-16T13:31:23.3969258Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[5] PASSED [ 94%]
2026-11-16T13:31:23.5684918Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-11-16T13:31:23.7177617Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026
```

**Error 2:**
```
2026-11-16T13:31:23.3969258Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[5] PASSED [ 94%]
2026-11-16T13:31:23.5684918Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-11-16T13:31:23.7177617Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026-11-16T13:31:23.8794466Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[5] FAILED [
```

**Error 3:**
```
2026-11-16T13:31:23.5684918Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-11-16T13:31:23.7177617Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026-11-16T13:31:23.8794466Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[5] FAILED [ 97%]
2026-11-16T13:31:23.8864957Z pySDC/projects/DAE/tests/test_problems.py::test_WSCC9_evaluation PASSED  [ 98%]
2026
```

**Error 4:**
```
2026-11-16T13:31:26.2972577Z >                           self.log(f"Located Switch at time {self.status.t_switch:.15f} is outside the range", S)
2026-11-16T13:31:26.2973137Z                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-16T13:31:26.2973644Z E                           TypeError: unsupported format string passed to numpy.ndarray.__format__
2026-11-16T13:31:26.2974016Z 
2026-11-16T13:31:26.2974185Z pySDC/projects/PinTSimE/switch_estimator.py:161:
```

**Error 5:**
```
2026-11-16T13:31:26.3038183Z >                           self.log(f"Located Switch at time {self.status.t_switch:.15f} is outside the range", S)
2026-11-16T13:31:26.3038747Z                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-16T13:31:26.3039264Z E                           TypeError: unsupported format string passed to numpy.ndarray.__format__
2026-11-16T13:31:26.3039631Z 
2026-11-16T13:31:26.3039815Z pySDC/projects/PinTSimE/switch_estimator.py:161:
```

### 4. user_monodomain_tests_linux

- **Job ID:** 133327870461
- **Started:** 2026-11-16T13:25:47Z
- **Completed:** 2026-11-16T13:26:45Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870461)

No specific error messages extracted. Check job logs for details.

### 5. user_cpu_tests_linux (pytorch, 3.10)

- **Job ID:** 133327870598
- **Started:** 2026-11-16T13:27:24Z
- **Completed:** 2026-11-16T13:28:20Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870598)

No specific error messages extracted. Check job logs for details.

### 6. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 133327870605
- **Started:** 2026-11-16T13:28:24Z
- **Completed:** 2026-11-16T13:31:04Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870605)

#### Error Details

**Error 1:**
```
2026-11-16T13:29:42.0850155Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-16T13:29:42.1062983Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-16T13:29:42.1757268Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:29:42.1915291Z pySDC/test
```

**Error 2:**
```
2026-11-16T13:29:42.1062983Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-16T13:29:42.1757268Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:29:42.1915291Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:29:42.2080945Z pySDC/te
```

**Error 3:**
```
2026-11-16T13:29:42.1757268Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:29:42.1915291Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:29:42.2080945Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:29:42.2246598Z pySDC/
```

**Error 4:**
```
2026-11-16T13:29:42.1915291Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:29:42.2080945Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:29:42.2246598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-16T13:29:42.2411164Z pySDC/
```

**Error 5:**
```
2026-11-16T13:29:42.2080945Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:29:42.2246598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-16T13:29:42.2411164Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-16T13:29:42.2573103Z pySDC/tests/
```

### 7. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 133327870616
- **Started:** 2026-11-16T13:25:47Z
- **Completed:** 2026-11-16T13:28:24Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870616)

#### Error Details

**Error 1:**
```
2026-11-16T13:27:10.0861088Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-16T13:27:10.1068940Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-16T13:27:10.1614333Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:27:10.1757159Z pySDC/test
```

**Error 2:**
```
2026-11-16T13:27:10.1068940Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-16T13:27:10.1614333Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:27:10.1757159Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:27:10.1888578Z pySDC/te
```

**Error 3:**
```
2026-11-16T13:27:10.1614333Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:27:10.1757159Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:27:10.1888578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:27:10.2022090Z pySDC/
```

**Error 4:**
```
2026-11-16T13:27:10.1757159Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:27:10.1888578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:27:10.2022090Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-16T13:27:10.2473977Z pySDC/
```

**Error 5:**
```
2026-11-16T13:27:10.1888578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:27:10.2022090Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-16T13:27:10.2473977Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-16T13:27:10.2600819Z pySDC/tests/
```

### 8. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 133327870631
- **Started:** 2026-11-16T13:27:20Z
- **Completed:** 2026-11-16T13:29:44Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/43875651376/job/133327870631)

#### Error Details

**Error 1:**
```
2026-11-16T13:28:34.1076034Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-16T13:28:34.1255174Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-16T13:28:34.1709183Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:28:34.1828668Z pySDC/test
```

**Error 2:**
```
2026-11-16T13:28:34.1255174Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-16T13:28:34.1709183Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:28:34.1828668Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:28:34.1945083Z pySDC/te
```

**Error 3:**
```
2026-11-16T13:28:34.1709183Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-16T13:28:34.1828668Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:28:34.1945083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:28:34.2061651Z pySDC/
```

**Error 4:**
```
2026-11-16T13:28:34.1828668Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-16T13:28:34.1945083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:28:34.2061651Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-16T13:28:34.2561801Z pySDC/
```

**Error 5:**
```
2026-11-16T13:28:34.1945083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-16T13:28:34.2061651Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-16T13:28:34.2561801Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-16T13:28:34.2691838Z pySDC/tests/
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
