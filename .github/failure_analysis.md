# Automated Test Failure Analysis

**Generated:** 2026-08-24T05:58:22.894763+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/32694364900

## Summary

- Total Jobs: 30
- Failed Jobs: 8

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 97333625075
- **Started:** 2026-08-24T05:40:26Z
- **Completed:** 2026-08-24T05:45:23Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625075)

#### Error Details

**Error 1:**
```
2026-08-24T05:41:45.1887949Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-08-24T05:41:45.1888159Z 
2026-08-24T05:41:47.2556079Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-08-24T05:41:47.2705920Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-08-24T05:41:47.2758976Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-08-24T05:43:22.1014139Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-08-24T05:43:23.5704005Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-24T05:43:23.6135162Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-24T05:43:23.6272186Z ../../
```

**Error 3:**
```
2026-08-24T05:43:23.5704005Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-24T05:43:23.6135162Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-24T05:43:23.6272186Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-24T05:43:23.6400148Z ../../../../reposi
```

**Error 4:**
```
2026-08-24T05:43:23.6135162Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-24T05:43:23.6272186Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-24T05:43:23.6400148Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-24T05:43:23.6535732Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-08-24T05:43:23.6272186Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-24T05:43:23.6400148Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-24T05:43:23.6535732Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-08-24T05:43:23.6671142Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 97333625180
- **Started:** 2026-08-24T05:40:26Z
- **Completed:** 2026-08-24T05:43:12Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625180)

#### Error Details

**Error 1:**
```
2026-08-24T05:41:41.0968918Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-24T05:41:41.1218907Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-24T05:41:41.2245209Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:41.2539792Z pySDC/test
```

**Error 2:**
```
2026-08-24T05:41:41.1218907Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-24T05:41:41.2245209Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:41.2539792Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:41.2836823Z pySDC/te
```

**Error 3:**
```
2026-08-24T05:41:41.2245209Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:41.2539792Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:41.2836823Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:41.3126439Z pySDC/
```

**Error 4:**
```
2026-08-24T05:41:41.2539792Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:41.2836823Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:41.3126439Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-24T05:41:41.3421361Z pySDC/
```

**Error 5:**
```
2026-08-24T05:41:41.2836823Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:41.3126439Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-24T05:41:41.3421361Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-24T05:41:41.3710259Z pySDC/tests/
```

### 3. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 97333625208
- **Started:** 2026-08-24T05:40:27Z
- **Completed:** 2026-08-24T05:56:45Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625208)

#### Error Details

**Error 1:**
```
2026-08-24T05:56:41.3896627Z                     res = fixturedef.cached_result[0]
2026-08-24T05:56:41.3897107Z >                   pickle.dump(res, f)
2026-08-24T05:56:41.3897912Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:56:41.3898615Z 
2026-08-24T05:56:41.3899208Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-24T05:56:41.4015173Z                     res = fixturedef.cached_result[0]
2026-08-24T05:56:41.4015917Z >                   pickle.dump(res, f)
2026-08-24T05:56:41.4016786Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:56:41.4017537Z 
2026-08-24T05:56:41.4018166Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-24T05:56:41.4110373Z                     res = fixturedef.cached_result[0]
2026-08-24T05:56:41.4110677Z >                   pickle.dump(res, f)
2026-08-24T05:56:41.4111157Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:56:41.4111555Z 
2026-08-24T05:56:41.4111891Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-24T05:56:41.4171887Z                     res = fixturedef.cached_result[0]
2026-08-24T05:56:41.4172181Z >                   pickle.dump(res, f)
2026-08-24T05:56:41.4172661Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:56:41.4173066Z 
2026-08-24T05:56:41.4173652Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-24T05:56:41.4234241Z                     res = fixturedef.cached_result[0]
2026-08-24T05:56:41.4234537Z >                   pickle.dump(res, f)
2026-08-24T05:56:41.4235014Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:56:41.4235421Z 
2026-08-24T05:56:41.4235763Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 4. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 97333625212
- **Started:** 2026-08-24T05:40:27Z
- **Completed:** 2026-08-24T05:57:27Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625212)

#### Error Details

**Error 1:**
```
2026-08-24T05:57:24.4671034Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:24.4671415Z >                   pickle.dump(res, f)
2026-08-24T05:57:24.4672335Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:24.4672877Z 
2026-08-24T05:57:24.4673319Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-24T05:57:24.4756809Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:24.4757100Z >                   pickle.dump(res, f)
2026-08-24T05:57:24.4757582Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:24.4757989Z 
2026-08-24T05:57:24.4758325Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-24T05:57:24.4816732Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:24.4817024Z >                   pickle.dump(res, f)
2026-08-24T05:57:24.4817502Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:24.4817904Z 
2026-08-24T05:57:24.4818235Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-24T05:57:24.4876725Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:24.4877014Z >                   pickle.dump(res, f)
2026-08-24T05:57:24.4877498Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:24.4877904Z 
2026-08-24T05:57:24.4878234Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-24T05:57:24.4937426Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:24.4937714Z >                   pickle.dump(res, f)
2026-08-24T05:57:24.4938198Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:24.4938622Z 
2026-08-24T05:57:24.4938950Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 5. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 97333625215
- **Started:** 2026-08-24T05:40:27Z
- **Completed:** 2026-08-24T05:43:36Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625215)

#### Error Details

**Error 1:**
```
2026-08-24T05:41:48.2468217Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-24T05:41:48.2750710Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-24T05:41:48.3533473Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:48.3857201Z pySDC/test
```

**Error 2:**
```
2026-08-24T05:41:48.2750710Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-24T05:41:48.3533473Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:48.3857201Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:48.4173827Z pySDC/te
```

**Error 3:**
```
2026-08-24T05:41:48.3533473Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:48.3857201Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:48.4173827Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:48.4490823Z pySDC/
```

**Error 4:**
```
2026-08-24T05:41:48.3857201Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:48.4173827Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:48.4490823Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-24T05:41:48.4809993Z pySDC/
```

**Error 5:**
```
2026-08-24T05:41:48.4173827Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:48.4490823Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-24T05:41:48.4809993Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-24T05:41:48.5130004Z pySDC/tests/
```

### 6. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 97333625236
- **Started:** 2026-08-24T05:40:27Z
- **Completed:** 2026-08-24T05:42:49Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625236)

#### Error Details

**Error 1:**
```
2026-08-24T05:41:42.9083227Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-24T05:41:42.9251922Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-24T05:41:42.9725800Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:42.9903429Z pySDC/test
```

**Error 2:**
```
2026-08-24T05:41:42.9251922Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-24T05:41:42.9725800Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:42.9903429Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:43.0079535Z pySDC/te
```

**Error 3:**
```
2026-08-24T05:41:42.9725800Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-24T05:41:42.9903429Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:43.0079535Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:43.0256468Z pySDC/
```

**Error 4:**
```
2026-08-24T05:41:42.9903429Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-24T05:41:43.0079535Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:43.0256468Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-24T05:41:43.0439709Z pySDC/
```

**Error 5:**
```
2026-08-24T05:41:43.0079535Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-24T05:41:43.0256468Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-24T05:41:43.0439709Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-24T05:41:43.0618290Z pySDC/tests/
```

### 7. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 97333625247
- **Started:** 2026-08-24T05:40:27Z
- **Completed:** 2026-08-24T05:55:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625247)

#### Error Details

**Error 1:**
```
2026-08-24T05:55:26.0595870Z                     res = fixturedef.cached_result[0]
2026-08-24T05:55:26.0596292Z >                   pickle.dump(res, f)
2026-08-24T05:55:26.0596993Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:55:26.0597594Z 
2026-08-24T05:55:26.0598097Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-24T05:55:26.0705724Z                     res = fixturedef.cached_result[0]
2026-08-24T05:55:26.0706218Z >                   pickle.dump(res, f)
2026-08-24T05:55:26.0707061Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:55:26.0707773Z 
2026-08-24T05:55:26.0708432Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-24T05:55:26.0797128Z                     res = fixturedef.cached_result[0]
2026-08-24T05:55:26.0797419Z >                   pickle.dump(res, f)
2026-08-24T05:55:26.0797903Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:55:26.0798301Z 
2026-08-24T05:55:26.0798660Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-24T05:55:26.0855775Z                     res = fixturedef.cached_result[0]
2026-08-24T05:55:26.0856060Z >                   pickle.dump(res, f)
2026-08-24T05:55:26.0856537Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:55:26.0857073Z 
2026-08-24T05:55:26.0857409Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-24T05:55:26.0914206Z                     res = fixturedef.cached_result[0]
2026-08-24T05:55:26.0914492Z >                   pickle.dump(res, f)
2026-08-24T05:55:26.0914966Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:55:26.0915366Z 
2026-08-24T05:55:26.0915692Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 8. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 97333625249
- **Started:** 2026-08-24T05:40:26Z
- **Completed:** 2026-08-24T05:57:05Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/32694364900/job/97333625249)

#### Error Details

**Error 1:**
```
2026-08-24T05:57:03.6159961Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:03.6160406Z >                   pickle.dump(res, f)
2026-08-24T05:57:03.6161318Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:03.6161976Z 
2026-08-24T05:57:03.6162522Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-24T05:57:03.6232826Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:03.6233267Z >                   pickle.dump(res, f)
2026-08-24T05:57:03.6234006Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:03.6234636Z 
2026-08-24T05:57:03.6235141Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-24T05:57:03.6305587Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:03.6305866Z >                   pickle.dump(res, f)
2026-08-24T05:57:03.6306318Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:03.6306693Z 
2026-08-24T05:57:03.6307013Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-24T05:57:03.6363298Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:03.6363582Z >                   pickle.dump(res, f)
2026-08-24T05:57:03.6364051Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:03.6364433Z 
2026-08-24T05:57:03.6364765Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-24T05:57:03.6424507Z                     res = fixturedef.cached_result[0]
2026-08-24T05:57:03.6424798Z >                   pickle.dump(res, f)
2026-08-24T05:57:03.6425255Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-24T05:57:03.6425634Z 
2026-08-24T05:57:03.6425959Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
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
