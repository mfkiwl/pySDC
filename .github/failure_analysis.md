# Automated Test Failure Analysis

**Generated:** 2026-11-23T16:04:31.722880+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/45208785392

## Summary

- Total Jobs: 30
- Failed Jobs: 7

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 137811626994
- **Started:** 2026-11-23T15:45:33Z
- **Completed:** 2026-11-23T15:48:44Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/45208785392/job/137811626994)

#### Error Details

**Error 1:**
```
2026-11-23T15:46:38.4670464Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-11-23T15:46:38.4670916Z 
2026-11-23T15:46:40.7884653Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-11-23T15:46:40.8064025Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-11-23T15:46:40.8136035Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-11-23T15:48:28.4184890Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-11-23T15:48:31.0243143Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-23T15:48:31.0616046Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-23T15:48:31.0782201Z ../../
```

**Error 3:**
```
2026-11-23T15:48:31.0243143Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-11-23T15:48:31.0616046Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-23T15:48:31.0782201Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-23T15:48:31.0943931Z ../../../../reposi
```

**Error 4:**
```
2026-11-23T15:48:31.0616046Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-11-23T15:48:31.0782201Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-23T15:48:31.0943931Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-23T15:48:31.1095233Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-11-23T15:48:31.0782201Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-11-23T15:48:31.0943931Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-11-23T15:48:31.1095233Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-11-23T15:48:31.1241366Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 137811627703
- **Started:** 2026-11-23T15:45:33Z
- **Completed:** 2026-11-23T15:48:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/45208785392/job/137811627703)

#### Error Details

**Error 1:**
```
2026-11-23T15:46:51.6833473Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-23T15:46:51.7078200Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-23T15:46:51.7640553Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:46:51.7803114Z pySDC/test
```

**Error 2:**
```
2026-11-23T15:46:51.7078200Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-23T15:46:51.7640553Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:46:51.7803114Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:46:51.7963028Z pySDC/te
```

**Error 3:**
```
2026-11-23T15:46:51.7640553Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:46:51.7803114Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:46:51.7963028Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:46:51.8135476Z pySDC/
```

**Error 4:**
```
2026-11-23T15:46:51.7803114Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:46:51.7963028Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:46:51.8135476Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-23T15:46:51.8722749Z pySDC/
```

**Error 5:**
```
2026-11-23T15:46:51.7963028Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:46:51.8135476Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-23T15:46:51.8722749Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-23T15:46:51.8884067Z pySDC/tests/
```

### 3. project_cpu_tests_linux (DAE)

- **Job ID:** 137811627742
- **Started:** 2026-11-23T15:45:33Z
- **Completed:** 2026-11-23T15:49:45Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/45208785392/job/137811627742)

#### Error Details

**Error 1:**
```
2026-11-23T15:49:38.4237373Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[4] PASSED [ 94%]
2026-11-23T15:49:38.6312725Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[5] PASSED [ 94%]
2026-11-23T15:49:38.8783429Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-11-23T15:49:39.1043706Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026
```

**Error 2:**
```
2026-11-23T15:49:38.6312725Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC[5] PASSED [ 94%]
2026-11-23T15:49:38.8783429Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-11-23T15:49:39.1043706Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026-11-23T15:49:39.3491429Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[5] FAILED [
```

**Error 3:**
```
2026-11-23T15:49:38.8783429Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[3] FAILED [ 95%]
2026-11-23T15:49:39.1043706Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[4] FAILED [ 96%]
2026-11-23T15:49:39.3491429Z pySDC/projects/DAE/tests/test_problems.py::test_DiscontinuousTestDAE_SDC_detection[5] FAILED [ 97%]
2026-11-23T15:49:39.3575694Z pySDC/projects/DAE/tests/test_problems.py::test_WSCC9_evaluation PASSED  [ 98%]
2026
```

**Error 4:**
```
2026-11-23T15:49:42.9258507Z >                           self.log(f"Located Switch at time {self.status.t_switch:.15f} is outside the range", S)
2026-11-23T15:49:42.9259430Z                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-23T15:49:42.9260269Z E                           TypeError: unsupported format string passed to numpy.ndarray.__format__
2026-11-23T15:49:42.9261118Z 
2026-11-23T15:49:42.9261423Z pySDC/projects/PinTSimE/switch_estimator.py:161:
```

**Error 5:**
```
2026-11-23T15:49:42.9360441Z >                           self.log(f"Located Switch at time {self.status.t_switch:.15f} is outside the range", S)
2026-11-23T15:49:42.9361215Z                                                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
2026-11-23T15:49:42.9361768Z E                           TypeError: unsupported format string passed to numpy.ndarray.__format__
2026-11-23T15:49:42.9362141Z 
2026-11-23T15:49:42.9362351Z pySDC/projects/PinTSimE/switch_estimator.py:161:
```

### 4. project_cpu_tests_linux (AllenCahn_Bayreuth)

- **Job ID:** 137811627842
- **Started:** 2026-11-23T15:45:33Z
- **Completed:** 2026-11-23T15:46:28Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/45208785392/job/137811627842)

No specific error messages extracted. Check job logs for details.

### 5. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 137811627997
- **Started:** 2026-11-23T15:46:49Z
- **Completed:** 2026-11-23T15:49:55Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/45208785392/job/137811627997)

#### Error Details

**Error 1:**
```
2026-11-23T15:48:10.5761247Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-23T15:48:10.6038482Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-23T15:48:10.6894994Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:48:10.7087377Z pySDC/test
```

**Error 2:**
```
2026-11-23T15:48:10.6038482Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-23T15:48:10.6894994Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:48:10.7087377Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:48:10.7277538Z pySDC/te
```

**Error 3:**
```
2026-11-23T15:48:10.6894994Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:48:10.7087377Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:48:10.7277538Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:48:10.7472145Z pySDC/
```

**Error 4:**
```
2026-11-23T15:48:10.7087377Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:48:10.7277538Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:48:10.7472145Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-23T15:48:10.7663516Z pySDC/
```

**Error 5:**
```
2026-11-23T15:48:10.7277538Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:48:10.7472145Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-23T15:48:10.7663516Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-23T15:48:10.7856281Z pySDC/tests/
```

### 6. user_cpu_tests_linux (petsc, 3.10)

- **Job ID:** 137811628087
- **Started:** 2026-11-23T15:46:42Z
- **Completed:** 2026-11-23T15:47:45Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/45208785392/job/137811628087)

No specific error messages extracted. Check job logs for details.

### 7. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 137811628211
- **Started:** 2026-11-23T15:46:37Z
- **Completed:** 2026-11-23T15:49:40Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/45208785392/job/137811628211)

#### Error Details

**Error 1:**
```
2026-11-23T15:47:59.6724291Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-11-23T15:47:59.6975978Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-23T15:47:59.7713653Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:47:59.7883531Z pySDC/test
```

**Error 2:**
```
2026-11-23T15:47:59.6975978Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-11-23T15:47:59.7713653Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:47:59.7883531Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:47:59.8052085Z pySDC/te
```

**Error 3:**
```
2026-11-23T15:47:59.7713653Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-11-23T15:47:59.7883531Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:47:59.8052085Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:47:59.8221677Z pySDC/
```

**Error 4:**
```
2026-11-23T15:47:59.7883531Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-11-23T15:47:59.8052085Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:47:59.8221677Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-23T15:47:59.8394598Z pySDC/
```

**Error 5:**
```
2026-11-23T15:47:59.8052085Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-11-23T15:47:59.8221677Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-11-23T15:47:59.8394598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-11-23T15:47:59.8905214Z pySDC/tests/
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
