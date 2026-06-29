# Automated Test Failure Analysis

**Generated:** 2026-06-29T10:05:26.514719+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/28363481903

## Summary

- Total Jobs: 30
- Failed Jobs: 4

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 84023527684
- **Started:** 2026-06-29T09:53:26Z
- **Completed:** 2026-06-29T10:00:24Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28363481903/job/84023527684)

#### Error Details

**Error 1:**
```
2026-06-29T09:54:48.6339616Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-06-29T09:54:48.6340075Z 
2026-06-29T09:54:52.0281844Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-06-29T09:54:52.0505051Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-06-29T09:54:52.0596377Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-06-29T09:57:22.5161412Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-06-29T09:57:24.6580709Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-29T09:57:24.7223971Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-29T09:57:24.7485633Z ../../
```

**Error 3:**
```
2026-06-29T09:57:24.6580709Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-29T09:57:24.7223971Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-29T09:57:24.7485633Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-29T09:57:24.7732318Z ../../../../reposi
```

**Error 4:**
```
2026-06-29T09:57:24.7223971Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-29T09:57:24.7485633Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-29T09:57:24.7732318Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-29T09:57:24.7982367Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-06-29T09:57:24.7485633Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-29T09:57:24.7732318Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-29T09:57:24.7982367Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-06-29T09:57:24.8232660Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 84023527772
- **Started:** 2026-06-29T09:50:31Z
- **Completed:** 2026-06-29T09:53:59Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28363481903/job/84023527772)

#### Error Details

**Error 1:**
```
2026-06-29T09:51:51.1597922Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-29T09:51:51.1866963Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-29T09:51:51.2777485Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-29T09:51:51.3085632Z pySDC/test
```

**Error 2:**
```
2026-06-29T09:51:51.1866963Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-29T09:51:51.2777485Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-29T09:51:51.3085632Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-29T09:51:51.3398755Z pySDC/te
```

**Error 3:**
```
2026-06-29T09:51:51.2777485Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-29T09:51:51.3085632Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-29T09:51:51.3398755Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-29T09:51:51.3708479Z pySDC/
```

**Error 4:**
```
2026-06-29T09:51:51.3085632Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-29T09:51:51.3398755Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-29T09:51:51.3708479Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-29T09:51:51.4033625Z pySDC/
```

**Error 5:**
```
2026-06-29T09:51:51.3398755Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-29T09:51:51.3708479Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-29T09:51:51.4033625Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-29T09:51:51.4352975Z pySDC/tests/
```

### 3. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 84023527789
- **Started:** 2026-06-29T09:50:30Z
- **Completed:** 2026-06-29T10:01:45Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28363481903/job/84023527789)

#### Error Details

**Error 1:**
```
2026-06-29T10:01:43.2232666Z                     res = fixturedef.cached_result[0]
2026-06-29T10:01:43.2233156Z >                   pickle.dump(res, f)
2026-06-29T10:01:43.2233989Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-29T10:01:43.2234712Z 
2026-06-29T10:01:43.2235303Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-06-29T10:01:43.2317627Z                     res = fixturedef.cached_result[0]
2026-06-29T10:01:43.2317909Z >                   pickle.dump(res, f)
2026-06-29T10:01:43.2318387Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-29T10:01:43.2318789Z 
2026-06-29T10:01:43.2319115Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-06-29T10:01:43.2385048Z                     res = fixturedef.cached_result[0]
2026-06-29T10:01:43.2385336Z >                   pickle.dump(res, f)
2026-06-29T10:01:43.2385811Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-29T10:01:43.2386337Z 
2026-06-29T10:01:43.2386667Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-06-29T10:01:43.2444033Z                     res = fixturedef.cached_result[0]
2026-06-29T10:01:43.2444317Z >                   pickle.dump(res, f)
2026-06-29T10:01:43.2444796Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-29T10:01:43.2445201Z 
2026-06-29T10:01:43.2445645Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-06-29T10:01:43.2511164Z                     res = fixturedef.cached_result[0]
2026-06-29T10:01:43.2511452Z >                   pickle.dump(res, f)
2026-06-29T10:01:43.2511932Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-29T10:01:43.2512335Z 
2026-06-29T10:01:43.2512667Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 4. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 84023527811
- **Started:** 2026-06-29T09:50:30Z
- **Completed:** 2026-06-29T09:53:12Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28363481903/job/84023527811)

#### Error Details

**Error 1:**
```
2026-06-29T09:51:43.5418433Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-29T09:51:43.5644165Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-29T09:51:43.6234083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-29T09:51:43.6507503Z pySDC/test
```

**Error 2:**
```
2026-06-29T09:51:43.5644165Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-29T09:51:43.6234083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-29T09:51:43.6507503Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-29T09:51:43.6782021Z pySDC/te
```

**Error 3:**
```
2026-06-29T09:51:43.6234083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-29T09:51:43.6507503Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-29T09:51:43.6782021Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-29T09:51:43.7052927Z pySDC/
```

**Error 4:**
```
2026-06-29T09:51:43.6507503Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-29T09:51:43.6782021Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-29T09:51:43.7052927Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-29T09:51:43.7324724Z pySDC/
```

**Error 5:**
```
2026-06-29T09:51:43.6782021Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-29T09:51:43.7052927Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-29T09:51:43.7324724Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-29T09:51:43.7599208Z pySDC/tests/
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
