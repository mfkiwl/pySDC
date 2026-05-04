# Automated Test Failure Analysis

**Generated:** 2026-05-04T08:06:50.312814+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/25307332400

## Summary

- Total Jobs: 30
- Failed Jobs: 4

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 74186129818
- **Started:** 2026-05-04T07:48:41Z
- **Completed:** 2026-05-04T07:55:36Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/25307332400/job/74186129818)

#### Error Details

**Error 1:**
```
2026-05-04T07:50:03.1144538Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-05-04T07:50:03.1144982Z 
2026-05-04T07:50:06.3853394Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-05-04T07:50:06.4079413Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-05-04T07:50:06.4167936Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-05-04T07:52:36.8476246Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-05-04T07:52:39.0120626Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-04T07:52:39.0760803Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-04T07:52:39.0996519Z ../../
```

**Error 3:**
```
2026-05-04T07:52:39.0120626Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-04T07:52:39.0760803Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-04T07:52:39.0996519Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-04T07:52:39.1223127Z ../../../../reposi
```

**Error 4:**
```
2026-05-04T07:52:39.0760803Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-04T07:52:39.0996519Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-04T07:52:39.1223127Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-04T07:52:39.1465679Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-05-04T07:52:39.0996519Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-04T07:52:39.1223127Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-04T07:52:39.1465679Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-05-04T07:52:39.1706149Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 74186129955
- **Started:** 2026-05-04T07:51:18Z
- **Completed:** 2026-05-04T07:54:23Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/25307332400/job/74186129955)

#### Error Details

**Error 1:**
```
2026-05-04T07:52:41.7384089Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-04T07:52:41.7656377Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-04T07:52:41.8617499Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:52:41.8909970Z pySDC/test
```

**Error 2:**
```
2026-05-04T07:52:41.7656377Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-04T07:52:41.8617499Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:52:41.8909970Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:52:41.9196711Z pySDC/te
```

**Error 3:**
```
2026-05-04T07:52:41.8617499Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:52:41.8909970Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:52:41.9196711Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:52:41.9487957Z pySDC/
```

**Error 4:**
```
2026-05-04T07:52:41.8909970Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:52:41.9196711Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:52:41.9487957Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-04T07:52:41.9778684Z pySDC/
```

**Error 5:**
```
2026-05-04T07:52:41.9196711Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:52:41.9487957Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-04T07:52:41.9778684Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-04T07:52:42.0072803Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 74186129976
- **Started:** 2026-05-04T07:51:54Z
- **Completed:** 2026-05-04T07:55:03Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/25307332400/job/74186129976)

#### Error Details

**Error 1:**
```
2026-05-04T07:53:09.3329967Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-04T07:53:09.3587208Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-04T07:53:09.4459763Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:53:09.4749598Z pySDC/test
```

**Error 2:**
```
2026-05-04T07:53:09.3587208Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-04T07:53:09.4459763Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:53:09.4749598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:53:09.5037949Z pySDC/te
```

**Error 3:**
```
2026-05-04T07:53:09.4459763Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:53:09.4749598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:53:09.5037949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:53:09.5331445Z pySDC/
```

**Error 4:**
```
2026-05-04T07:53:09.4749598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:53:09.5037949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:53:09.5331445Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-04T07:53:09.5620288Z pySDC/
```

**Error 5:**
```
2026-05-04T07:53:09.5037949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:53:09.5331445Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-04T07:53:09.5620288Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-04T07:53:09.5913049Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 74186129983
- **Started:** 2026-05-04T07:51:30Z
- **Completed:** 2026-05-04T07:54:08Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/25307332400/job/74186129983)

#### Error Details

**Error 1:**
```
2026-05-04T07:52:39.6224213Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-04T07:52:39.6479223Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-04T07:52:39.7233502Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:52:39.7543242Z pySDC/test
```

**Error 2:**
```
2026-05-04T07:52:39.6479223Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-04T07:52:39.7233502Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:52:39.7543242Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:52:39.7849732Z pySDC/te
```

**Error 3:**
```
2026-05-04T07:52:39.7233502Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-04T07:52:39.7543242Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:52:39.7849732Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:52:39.8158218Z pySDC/
```

**Error 4:**
```
2026-05-04T07:52:39.7543242Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-04T07:52:39.7849732Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:52:39.8158218Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-04T07:52:39.8467631Z pySDC/
```

**Error 5:**
```
2026-05-04T07:52:39.7849732Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-04T07:52:39.8158218Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-04T07:52:39.8467631Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-04T07:52:39.8783639Z pySDC/tests/
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
