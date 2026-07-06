# Automated Test Failure Analysis

**Generated:** 2026-07-06T09:16:48.403285+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/28780078903

## Summary

- Total Jobs: 30
- Failed Jobs: 6

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 85333341288
- **Started:** 2026-07-06T09:01:37Z
- **Completed:** 2026-07-06T09:08:59Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28780078903/job/85333341288)

#### Error Details

**Error 1:**
```
2026-07-06T09:03:03.6086818Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-07-06T09:03:03.6087388Z 
2026-07-06T09:03:07.0590884Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-07-06T09:03:07.0819876Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-07-06T09:03:07.0912804Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-07-06T09:05:47.4857781Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-07-06T09:05:51.4506848Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-06T09:05:51.5110794Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-06T09:05:51.5344876Z ../../
```

**Error 3:**
```
2026-07-06T09:05:51.4506848Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-06T09:05:51.5110794Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-06T09:05:51.5344876Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-06T09:05:51.5571402Z ../../../../reposi
```

**Error 4:**
```
2026-07-06T09:05:51.5110794Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-06T09:05:51.5344876Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-06T09:05:51.5571402Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-06T09:05:51.5813605Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-07-06T09:05:51.5344876Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-06T09:05:51.5571402Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-06T09:05:51.5813605Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-07-06T09:05:51.6061261Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 85333341364
- **Started:** 2026-07-06T09:03:15Z
- **Completed:** 2026-07-06T09:05:12Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28780078903/job/85333341364)

#### Error Details

**Error 1:**
```
2026-07-06T09:04:15.4863985Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-06T09:04:15.4994481Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-06T09:04:15.5454151Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-06T09:04:15.5608741Z pySDC/test
```

**Error 2:**
```
2026-07-06T09:04:15.4994481Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-06T09:04:15.5454151Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-06T09:04:15.5608741Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-06T09:04:15.5761702Z pySDC/te
```

**Error 3:**
```
2026-07-06T09:04:15.5454151Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-06T09:04:15.5608741Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-06T09:04:15.5761702Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-06T09:04:15.5914286Z pySDC/
```

**Error 4:**
```
2026-07-06T09:04:15.5608741Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-06T09:04:15.5761702Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-06T09:04:15.5914286Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-06T09:04:15.6065950Z pySDC/
```

**Error 5:**
```
2026-07-06T09:04:15.5761702Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-06T09:04:15.5914286Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-06T09:04:15.6065950Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-06T09:04:15.6222243Z pySDC/tests/
```

### 3. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 85333341373
- **Started:** 2026-07-06T09:01:37Z
- **Completed:** 2026-07-06T09:13:36Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28780078903/job/85333341373)

#### Error Details

**Error 1:**
```
2026-07-06T09:13:33.9839107Z                     res = fixturedef.cached_result[0]
2026-07-06T09:13:33.9839630Z >                   pickle.dump(res, f)
2026-07-06T09:13:33.9840712Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:13:33.9841465Z 
2026-07-06T09:13:33.9842081Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-07-06T09:13:33.9930886Z                     res = fixturedef.cached_result[0]
2026-07-06T09:13:33.9931166Z >                   pickle.dump(res, f)
2026-07-06T09:13:33.9931637Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:13:33.9932034Z 
2026-07-06T09:13:33.9932363Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-07-06T09:13:33.9994027Z                     res = fixturedef.cached_result[0]
2026-07-06T09:13:33.9994307Z >                   pickle.dump(res, f)
2026-07-06T09:13:33.9994781Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:13:33.9995180Z 
2026-07-06T09:13:33.9995509Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-07-06T09:13:34.0061760Z                     res = fixturedef.cached_result[0]
2026-07-06T09:13:34.0062039Z >                   pickle.dump(res, f)
2026-07-06T09:13:34.0062515Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:13:34.0062912Z 
2026-07-06T09:13:34.0063240Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-07-06T09:13:34.0120610Z                     res = fixturedef.cached_result[0]
2026-07-06T09:13:34.0120889Z >                   pickle.dump(res, f)
2026-07-06T09:13:34.0121364Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:13:34.0121766Z 
2026-07-06T09:13:34.0122085Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 4. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 85333341402
- **Started:** 2026-07-06T09:01:36Z
- **Completed:** 2026-07-06T09:12:40Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28780078903/job/85333341402)

#### Error Details

**Error 1:**
```
2026-07-06T09:12:37.3223575Z                     res = fixturedef.cached_result[0]
2026-07-06T09:12:37.3223921Z >                   pickle.dump(res, f)
2026-07-06T09:12:37.3224500Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:12:37.3224989Z 
2026-07-06T09:12:37.3225396Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-07-06T09:12:37.3290533Z                     res = fixturedef.cached_result[0]
2026-07-06T09:12:37.3290825Z >                   pickle.dump(res, f)
2026-07-06T09:12:37.3291305Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:12:37.3291706Z 
2026-07-06T09:12:37.3292038Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-07-06T09:12:37.3362496Z                     res = fixturedef.cached_result[0]
2026-07-06T09:12:37.3362790Z >                   pickle.dump(res, f)
2026-07-06T09:12:37.3363282Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:12:37.3363693Z 
2026-07-06T09:12:37.3364028Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-07-06T09:12:37.3422755Z                     res = fixturedef.cached_result[0]
2026-07-06T09:12:37.3423043Z >                   pickle.dump(res, f)
2026-07-06T09:12:37.3423530Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:12:37.3424080Z 
2026-07-06T09:12:37.3424407Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-07-06T09:12:37.3483110Z                     res = fixturedef.cached_result[0]
2026-07-06T09:12:37.3483402Z >                   pickle.dump(res, f)
2026-07-06T09:12:37.3483878Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:12:37.3484278Z 
2026-07-06T09:12:37.3484608Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 5. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 85333341422
- **Started:** 2026-07-06T09:03:32Z
- **Completed:** 2026-07-06T09:16:02Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28780078903/job/85333341422)

#### Error Details

**Error 1:**
```
2026-07-06T09:16:00.6401152Z                     res = fixturedef.cached_result[0]
2026-07-06T09:16:00.6401948Z >                   pickle.dump(res, f)
2026-07-06T09:16:00.6402957Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:16:00.6403717Z 
2026-07-06T09:16:00.6404348Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-07-06T09:16:00.6469479Z                     res = fixturedef.cached_result[0]
2026-07-06T09:16:00.6470185Z >                   pickle.dump(res, f)
2026-07-06T09:16:00.6471106Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:16:00.6471844Z 
2026-07-06T09:16:00.6472450Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-07-06T09:16:00.6541298Z                     res = fixturedef.cached_result[0]
2026-07-06T09:16:00.6541580Z >                   pickle.dump(res, f)
2026-07-06T09:16:00.6542044Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:16:00.6542437Z 
2026-07-06T09:16:00.6542766Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-07-06T09:16:00.6609467Z                     res = fixturedef.cached_result[0]
2026-07-06T09:16:00.6609916Z >                   pickle.dump(res, f)
2026-07-06T09:16:00.6610401Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:16:00.6610799Z 
2026-07-06T09:16:00.6611136Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-07-06T09:16:00.6669782Z                     res = fixturedef.cached_result[0]
2026-07-06T09:16:00.6670071Z >                   pickle.dump(res, f)
2026-07-06T09:16:00.6670537Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:16:00.6670932Z 
2026-07-06T09:16:00.6671259Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 6. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 85333341432
- **Started:** 2026-07-06T09:03:08Z
- **Completed:** 2026-07-06T09:15:09Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/28780078903/job/85333341432)

#### Error Details

**Error 1:**
```
2026-07-06T09:15:07.5273694Z                     res = fixturedef.cached_result[0]
2026-07-06T09:15:07.5274177Z >                   pickle.dump(res, f)
2026-07-06T09:15:07.5274971Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:15:07.5275655Z 
2026-07-06T09:15:07.5276233Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-07-06T09:15:07.5341586Z                     res = fixturedef.cached_result[0]
2026-07-06T09:15:07.5341867Z >                   pickle.dump(res, f)
2026-07-06T09:15:07.5342332Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:15:07.5342725Z 
2026-07-06T09:15:07.5343055Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-07-06T09:15:07.5416980Z                     res = fixturedef.cached_result[0]
2026-07-06T09:15:07.5417266Z >                   pickle.dump(res, f)
2026-07-06T09:15:07.5417723Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:15:07.5418120Z 
2026-07-06T09:15:07.5418449Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-07-06T09:15:07.5484895Z                     res = fixturedef.cached_result[0]
2026-07-06T09:15:07.5485175Z >                   pickle.dump(res, f)
2026-07-06T09:15:07.5485640Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:15:07.5486031Z 
2026-07-06T09:15:07.5486352Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-07-06T09:15:07.5544304Z                     res = fixturedef.cached_result[0]
2026-07-06T09:15:07.5544583Z >                   pickle.dump(res, f)
2026-07-06T09:15:07.5545045Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-06T09:15:07.5545434Z 
2026-07-06T09:15:07.5545763Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
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
