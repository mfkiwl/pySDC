# Automated Test Failure Analysis

**Generated:** 2026-07-13T08:33:27.519906+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/29234962396

## Summary

- Total Jobs: 30
- Failed Jobs: 6

## Failed Jobs

### 1. user_monodomain_tests_linux

- **Job ID:** 86767405629
- **Started:** 2026-07-13T08:18:13Z
- **Completed:** 2026-07-13T08:19:10Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29234962396/job/86767405629)

No specific error messages extracted. Check job logs for details.

### 2. user_firedrake_tests

- **Job ID:** 86767405655
- **Started:** 2026-07-13T08:18:14Z
- **Completed:** 2026-07-13T08:24:32Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29234962396/job/86767405655)

#### Error Details

**Error 1:**
```
2026-07-13T08:19:55.3769111Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-07-13T08:19:55.3769534Z 
2026-07-13T08:19:58.3102894Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-07-13T08:19:58.3280706Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-07-13T08:19:58.3349561Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-07-13T08:22:01.9149154Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-07-13T08:22:03.7547836Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-13T08:22:03.8033680Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-13T08:22:03.8212660Z ../../
```

**Error 3:**
```
2026-07-13T08:22:03.7547836Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-13T08:22:03.8033680Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-13T08:22:03.8212660Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-13T08:22:03.8388053Z ../../../../reposi
```

**Error 4:**
```
2026-07-13T08:22:03.8033680Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-13T08:22:03.8212660Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-13T08:22:03.8388053Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-13T08:22:03.8576454Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-07-13T08:22:03.8212660Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-13T08:22:03.8388053Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-13T08:22:03.8576454Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-07-13T08:22:03.8768632Z ../../../../repositories/py
```

### 3. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 86767406072
- **Started:** 2026-07-13T08:20:45Z
- **Completed:** 2026-07-13T08:22:40Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29234962396/job/86767406072)

#### Error Details

**Error 1:**
```
2026-07-13T08:21:44.0864092Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-13T08:21:44.0997128Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-13T08:21:44.1575611Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:21:44.1732875Z pySDC/test
```

**Error 2:**
```
2026-07-13T08:21:44.0997128Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-13T08:21:44.1575611Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:21:44.1732875Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:21:44.1890368Z pySDC/te
```

**Error 3:**
```
2026-07-13T08:21:44.1575611Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:21:44.1732875Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:21:44.1890368Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:21:44.2049326Z pySDC/
```

**Error 4:**
```
2026-07-13T08:21:44.1732875Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:21:44.1890368Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:21:44.2049326Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-13T08:21:44.2207119Z pySDC/
```

**Error 5:**
```
2026-07-13T08:21:44.1890368Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:21:44.2049326Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-13T08:21:44.2207119Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-13T08:21:44.2365733Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 86767406083
- **Started:** 2026-07-13T08:18:13Z
- **Completed:** 2026-07-13T08:21:23Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29234962396/job/86767406083)

#### Error Details

**Error 1:**
```
2026-07-13T08:19:30.9083861Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-13T08:19:30.9335232Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-13T08:19:31.0215949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:19:31.0501784Z pySDC/test
```

**Error 2:**
```
2026-07-13T08:19:30.9335232Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-13T08:19:31.0215949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:19:31.0501784Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:19:31.0790065Z pySDC/te
```

**Error 3:**
```
2026-07-13T08:19:31.0215949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:19:31.0501784Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:19:31.0790065Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:19:31.1077961Z pySDC/
```

**Error 4:**
```
2026-07-13T08:19:31.0501784Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:19:31.0790065Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:19:31.1077961Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-13T08:19:31.1369198Z pySDC/
```

**Error 5:**
```
2026-07-13T08:19:31.0790065Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:19:31.1077961Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-13T08:19:31.1369198Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-13T08:19:31.1655937Z pySDC/tests/
```

### 5. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 86767406091
- **Started:** 2026-07-13T08:20:34Z
- **Completed:** 2026-07-13T08:32:36Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29234962396/job/86767406091)

#### Error Details

**Error 1:**
```
2026-07-13T08:32:34.1864569Z                     res = fixturedef.cached_result[0]
2026-07-13T08:32:34.1865062Z >                   pickle.dump(res, f)
2026-07-13T08:32:34.1865908Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-13T08:32:34.1866647Z 
2026-07-13T08:32:34.1867248Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-07-13T08:32:34.1942305Z                     res = fixturedef.cached_result[0]
2026-07-13T08:32:34.1942792Z >                   pickle.dump(res, f)
2026-07-13T08:32:34.1943634Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-13T08:32:34.1944363Z 
2026-07-13T08:32:34.1944943Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-07-13T08:32:34.2016033Z                     res = fixturedef.cached_result[0]
2026-07-13T08:32:34.2016318Z >                   pickle.dump(res, f)
2026-07-13T08:32:34.2016804Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-13T08:32:34.2017210Z 
2026-07-13T08:32:34.2017541Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-07-13T08:32:34.2075805Z                     res = fixturedef.cached_result[0]
2026-07-13T08:32:34.2076098Z >                   pickle.dump(res, f)
2026-07-13T08:32:34.2076728Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-13T08:32:34.2077134Z 
2026-07-13T08:32:34.2077466Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-07-13T08:32:34.2136722Z                     res = fixturedef.cached_result[0]
2026-07-13T08:32:34.2137011Z >                   pickle.dump(res, f)
2026-07-13T08:32:34.2137493Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-13T08:32:34.2137903Z 
2026-07-13T08:32:34.2138235Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 6. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 86767406125
- **Started:** 2026-07-13T08:20:03Z
- **Completed:** 2026-07-13T08:22:59Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29234962396/job/86767406125)

#### Error Details

**Error 1:**
```
2026-07-13T08:21:17.1185953Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-13T08:21:17.1451887Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-13T08:21:17.2221512Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:21:17.2537097Z pySDC/test
```

**Error 2:**
```
2026-07-13T08:21:17.1451887Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-13T08:21:17.2221512Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:21:17.2537097Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:21:17.2850709Z pySDC/te
```

**Error 3:**
```
2026-07-13T08:21:17.2221512Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-13T08:21:17.2537097Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:21:17.2850709Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:21:17.3165178Z pySDC/
```

**Error 4:**
```
2026-07-13T08:21:17.2537097Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-13T08:21:17.2850709Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:21:17.3165178Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-13T08:21:17.3476777Z pySDC/
```

**Error 5:**
```
2026-07-13T08:21:17.2850709Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-13T08:21:17.3165178Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-13T08:21:17.3476777Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-13T08:21:17.3789458Z pySDC/tests/
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
