# Automated Test Failure Analysis

**Generated:** 2026-10-26T11:09:57.159453+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/40310478105

## Summary

- Total Jobs: 30
- Failed Jobs: 9

## Failed Jobs

### 1. user_cpu_tests_linux (petsc, 3.11)

- **Job ID:** 121530118089
- **Started:** 2026-10-26T10:50:12Z
- **Completed:** 2026-10-26T10:52:41Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118089)

No specific error messages extracted. Check job logs for details.

### 2. user_firedrake_tests

- **Job ID:** 121530118297
- **Started:** 2026-10-26T10:50:13Z
- **Completed:** 2026-10-26T10:54:47Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118297)

#### Error Details

**Error 1:**
```
2026-10-26T10:51:40.0766248Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-10-26T10:51:40.0766863Z 
2026-10-26T10:51:43.7163204Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-10-26T10:51:43.7403280Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-10-26T10:51:43.7504284Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-10-26T10:54:25.7770515Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-10-26T10:54:28.4747148Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-10-26T10:54:28.5386844Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-10-26T10:54:28.5672187Z ../../
```

**Error 3:**
```
2026-10-26T10:54:28.4747148Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-10-26T10:54:28.5386844Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-10-26T10:54:28.5672187Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-10-26T10:54:28.5955222Z ../../../../reposi
```

**Error 4:**
```
2026-10-26T10:54:28.5386844Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-10-26T10:54:28.5672187Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-10-26T10:54:28.5955222Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-10-26T10:54:28.6198758Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-10-26T10:54:28.5672187Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-10-26T10:54:28.5955222Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-10-26T10:54:28.6198758Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-10-26T10:54:28.6424262Z ../../../../repositories/py
```

### 3. project_cpu_tests_linux (RayleighBenard)

- **Job ID:** 121530118400
- **Started:** 2026-10-26T10:50:12Z
- **Completed:** 2026-10-26T10:50:54Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118400)

No specific error messages extracted. Check job logs for details.

### 4. project_cpu_tests_linux (PinTSimE)

- **Job ID:** 121530118479
- **Started:** 2026-10-26T10:50:13Z
- **Completed:** 2026-10-26T10:51:25Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118479)

#### Error Details

**Error 1:**
```
2026-10-26T10:51:02.1207224Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[4] PASSED [ 11%]
2026-10-26T10:51:02.1244217Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[5] PASSED [ 13%]
2026-10-26T10:51:02.1773251Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-10-26T10:51:02.2087261Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAIL
```

**Error 2:**
```
2026-10-26T10:51:02.1244217Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionBoundary[5] PASSED [ 13%]
2026-10-26T10:51:02.1773251Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-10-26T10:51:02.2087261Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-10-26T10:51:02.2404518Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e
```

**Error 3:**
```
2026-10-26T10:51:02.1773251Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-08] FAILED [ 15%]
2026-10-26T10:51:02.2087261Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-10-26T10:51:02.2404518Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-10-26T10:51:02.2708746Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

**Error 4:**
```
2026-10-26T10:51:02.2087261Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-09] FAILED [ 18%]
2026-10-26T10:51:02.2404518Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-10-26T10:51:02.2708746Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-11] FAILED [ 22%]
2026-10-26T10:51:02.3030430Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

**Error 5:**
```
2026-10-26T10:51:02.2404518Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-10] FAILED [ 20%]
2026-10-26T10:51:02.2708746Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-11] FAILED [ 22%]
2026-10-26T10:51:02.3030430Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOBATTO-3-1e-12] FAILED [ 25%]
2026-10-26T10:51:02.3342603Z pySDC/projects/PinTSimE/tests/test_SwitchEstimator.py::testDetectionODE[LOB
```

### 5. project_cpu_tests_linux (DAE)

- **Job ID:** 121530118494
- **Started:** 2026-10-26T10:50:12Z
- **Completed:** 2026-10-26T10:53:15Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118494)

#### Error Details

**Error 1:**
```
2026-10-26T10:53:10.0461223Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[4] PASSED [ 94%]
2026-10-26T10:53:10.1858838Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[5] PASSED [ 94%]
2026-10-26T10:53:10.3796041Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-10-26T10:53:10.5531265Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026
```

**Error 2:**
```
2026-10-26T10:53:10.1858838Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[5] PASSED [ 94%]
2026-10-26T10:53:10.3796041Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-10-26T10:53:10.5531265Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026-10-26T10:53:10.7413843Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[5] FAILED [
```

**Error 3:**
```
2026-10-26T10:53:10.3796041Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-10-26T10:53:10.5531265Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026-10-26T10:53:10.7413843Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[5] FAILED [ 97%]
2026-10-26T10:53:10.7486753Z pySDC/projects/DAE/tests/test_problems.py::test_WSCC9_evaluation PASSED  [ 98%]
2026
```

**Error 4:**
```
2026-10-26T10:53:13.2091216Z >                           self.log(f"Located Switch at time {self.status.t_switch:.15f} is outside the range", S)
2026-10-26T10:53:13.2091597Z                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-26T10:53:13.2091971Z E                           TypeError: unsupported format string passed to numpy.ndarray.__format__
2026-10-26T10:53:13.2092222Z 
2026-10-26T10:53:13.2092346Z pySDC/projects/PinTSimE/switch_estimator.py:161:
```

**Error 5:**
```
2026-10-26T10:53:13.2136776Z >                           self.log(f"Located Switch at time {self.status.t_switch:.15f} is outside the range", S)
2026-10-26T10:53:13.2137142Z                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-26T10:53:13.2137500Z E                           TypeError: unsupported format string passed to numpy.ndarray.__format__
2026-10-26T10:53:13.2137744Z 
2026-10-26T10:53:13.2137871Z pySDC/projects/PinTSimE/switch_estimator.py:161:
```

### 6. user_cpu_tests_linux (pytorch, 3.11)

- **Job ID:** 121530118546
- **Started:** 2026-10-26T10:50:13Z
- **Completed:** 2026-10-26T10:51:04Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118546)

No specific error messages extracted. Check job logs for details.

### 7. user_cpu_tests_linux (petsc, 3.12)

- **Job ID:** 121530118709
- **Started:** 2026-10-26T10:50:13Z
- **Completed:** 2026-10-26T10:50:54Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118709)

No specific error messages extracted. Check job logs for details.

### 8. project_cpu_tests_linux (parallelSDC)

- **Job ID:** 121530118781
- **Started:** 2026-10-26T10:50:13Z
- **Completed:** 2026-10-26T10:50:53Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118781)

No specific error messages extracted. Check job logs for details.

### 9. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 121530118804
- **Started:** 2026-10-26T10:51:44Z
- **Completed:** 2026-10-26T10:52:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/40310478105/job/121530118804)

No specific error messages extracted. Check job logs for details.

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
