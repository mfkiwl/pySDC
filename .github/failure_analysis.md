# Automated Test Failure Analysis

**Generated:** 2026-09-14T10:43:51.838320+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/34833036623

## Summary

- Total Jobs: 30
- Failed Jobs: 12

## Failed Jobs

### 1. user_cpu_tests_linux (petsc, 3.12)

- **Job ID:** 103940541163
- **Started:** 2026-09-14T10:24:47Z
- **Completed:** 2026-09-14T10:25:45Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541163)

No specific error messages extracted. Check job logs for details.

### 2. user_cpu_tests_linux (petsc, 3.13)

- **Job ID:** 103940541192
- **Started:** 2026-09-14T10:24:47Z
- **Completed:** 2026-09-14T10:25:39Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541192)

No specific error messages extracted. Check job logs for details.

### 3. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 103940541199
- **Started:** 2026-09-14T10:24:46Z
- **Completed:** 2026-09-14T10:40:01Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541199)

#### Error Details

**Error 1:**
```
2026-09-14T10:39:58.6042838Z                     res = fixturedef.cached_result[0]
2026-09-14T10:39:58.6043290Z >                   pickle.dump(res, f)
2026-09-14T10:39:58.6044063Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:39:58.6044728Z 
2026-09-14T10:39:58.6045189Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-09-14T10:39:58.6124332Z                     res = fixturedef.cached_result[0]
2026-09-14T10:39:58.6124628Z >                   pickle.dump(res, f)
2026-09-14T10:39:58.6125186Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:39:58.6125865Z 
2026-09-14T10:39:58.6126416Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-09-14T10:39:58.6184942Z                     res = fixturedef.cached_result[0]
2026-09-14T10:39:58.6185229Z >                   pickle.dump(res, f)
2026-09-14T10:39:58.6185701Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:39:58.6186092Z 
2026-09-14T10:39:58.6186415Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-09-14T10:39:58.6243780Z                     res = fixturedef.cached_result[0]
2026-09-14T10:39:58.6244071Z >                   pickle.dump(res, f)
2026-09-14T10:39:58.6244566Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:39:58.6245121Z 
2026-09-14T10:39:58.6245454Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-09-14T10:39:58.6302811Z                     res = fixturedef.cached_result[0]
2026-09-14T10:39:58.6303096Z >                   pickle.dump(res, f)
2026-09-14T10:39:58.6303574Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:39:58.6303972Z 
2026-09-14T10:39:58.6304294Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 4. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 103940541203
- **Started:** 2026-09-14T10:24:47Z
- **Completed:** 2026-09-14T10:27:48Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541203)

#### Error Details

**Error 1:**
```
2026-09-14T10:26:06.0521145Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-14T10:26:06.0787576Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-14T10:26:06.1674829Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:06.1965863Z pySDC/test
```

**Error 2:**
```
2026-09-14T10:26:06.0787576Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-14T10:26:06.1674829Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:06.1965863Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:06.2253504Z pySDC/te
```

**Error 3:**
```
2026-09-14T10:26:06.1674829Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:06.1965863Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:06.2253504Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:06.2537441Z pySDC/
```

**Error 4:**
```
2026-09-14T10:26:06.1965863Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:06.2253504Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:06.2537441Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-14T10:26:06.2825823Z pySDC/
```

**Error 5:**
```
2026-09-14T10:26:06.2253504Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:06.2537441Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-14T10:26:06.2825823Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-14T10:26:06.3112800Z pySDC/tests/
```

### 5. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 103940541222
- **Started:** 2026-09-14T10:24:47Z
- **Completed:** 2026-09-14T10:41:51Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541222)

#### Error Details

**Error 1:**
```
2026-09-14T10:41:48.6022285Z                     res = fixturedef.cached_result[0]
2026-09-14T10:41:48.6022587Z >                   pickle.dump(res, f)
2026-09-14T10:41:48.6023197Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:41:48.6023604Z 
2026-09-14T10:41:48.6023959Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-09-14T10:41:48.6109870Z                     res = fixturedef.cached_result[0]
2026-09-14T10:41:48.6110153Z >                   pickle.dump(res, f)
2026-09-14T10:41:48.6110636Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:41:48.6111049Z 
2026-09-14T10:41:48.6111383Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-09-14T10:41:48.6169608Z                     res = fixturedef.cached_result[0]
2026-09-14T10:41:48.6169891Z >                   pickle.dump(res, f)
2026-09-14T10:41:48.6170367Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:41:48.6170764Z 
2026-09-14T10:41:48.6171095Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-09-14T10:41:48.6237698Z                     res = fixturedef.cached_result[0]
2026-09-14T10:41:48.6237984Z >                   pickle.dump(res, f)
2026-09-14T10:41:48.6238473Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:41:48.6238878Z 
2026-09-14T10:41:48.6239208Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-09-14T10:41:48.6299080Z                     res = fixturedef.cached_result[0]
2026-09-14T10:41:48.6299368Z >                   pickle.dump(res, f)
2026-09-14T10:41:48.6299849Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:41:48.6300252Z 
2026-09-14T10:41:48.6300578Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 6. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 103940541236
- **Started:** 2026-09-14T10:24:49Z
- **Completed:** 2026-09-14T10:27:49Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541236)

#### Error Details

**Error 1:**
```
2026-09-14T10:26:05.3278105Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-14T10:26:05.3536413Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-14T10:26:05.4282410Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:05.4579990Z pySDC/test
```

**Error 2:**
```
2026-09-14T10:26:05.3536413Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-14T10:26:05.4282410Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:05.4579990Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:05.4876603Z pySDC/te
```

**Error 3:**
```
2026-09-14T10:26:05.4282410Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:05.4579990Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:05.4876603Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:05.5174719Z pySDC/
```

**Error 4:**
```
2026-09-14T10:26:05.4579990Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:05.4876603Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:05.5174719Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-14T10:26:05.5478471Z pySDC/
```

**Error 5:**
```
2026-09-14T10:26:05.4876603Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:05.5174719Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-14T10:26:05.5478471Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-14T10:26:05.5772242Z pySDC/tests/
```

### 7. user_cpu_tests_linux (petsc, 3.11)

- **Job ID:** 103940541251
- **Started:** 2026-09-14T10:24:47Z
- **Completed:** 2026-09-14T10:25:42Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541251)

No specific error messages extracted. Check job logs for details.

### 8. user_firedrake_tests

- **Job ID:** 103940541277
- **Started:** 2026-09-14T10:25:44Z
- **Completed:** 2026-09-14T10:33:17Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541277)

#### Error Details

**Error 1:**
```
2026-09-14T10:27:11.5230521Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-09-14T10:27:11.5231297Z 
2026-09-14T10:27:15.0659876Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-09-14T10:27:15.0893256Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-09-14T10:27:15.0992027Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-09-14T10:30:06.2967583Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-09-14T10:30:08.4722549Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-14T10:30:08.5336150Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-14T10:30:08.5574505Z ../../
```

**Error 3:**
```
2026-09-14T10:30:08.4722549Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-14T10:30:08.5336150Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-14T10:30:08.5574505Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-14T10:30:08.5823025Z ../../../../reposi
```

**Error 4:**
```
2026-09-14T10:30:08.5336150Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-14T10:30:08.5574505Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-14T10:30:08.5823025Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-14T10:30:08.6087379Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-09-14T10:30:08.5574505Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-14T10:30:08.5823025Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-14T10:30:08.6087379Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-09-14T10:30:08.6352018Z ../../../../repositories/py
```

### 9. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 103940541288
- **Started:** 2026-09-14T10:25:44Z
- **Completed:** 2026-09-14T10:28:26Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541288)

#### Error Details

**Error 1:**
```
2026-09-14T10:26:56.1300844Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-14T10:26:56.1547323Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-14T10:26:56.2524707Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:56.2807315Z pySDC/test
```

**Error 2:**
```
2026-09-14T10:26:56.1547323Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-14T10:26:56.2524707Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:56.2807315Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:56.3087337Z pySDC/te
```

**Error 3:**
```
2026-09-14T10:26:56.2524707Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-14T10:26:56.2807315Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:56.3087337Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:56.3367176Z pySDC/
```

**Error 4:**
```
2026-09-14T10:26:56.2807315Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-14T10:26:56.3087337Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:56.3367176Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-14T10:26:56.3646986Z pySDC/
```

**Error 5:**
```
2026-09-14T10:26:56.3087337Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-14T10:26:56.3367176Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-14T10:26:56.3646986Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-14T10:26:56.3922906Z pySDC/tests/
```

### 10. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 103940541322
- **Started:** 2026-09-14T10:25:45Z
- **Completed:** 2026-09-14T10:42:02Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541322)

#### Error Details

**Error 1:**
```
2026-09-14T10:42:00.3721961Z                     res = fixturedef.cached_result[0]
2026-09-14T10:42:00.3722454Z >                   pickle.dump(res, f)
2026-09-14T10:42:00.3723081Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:42:00.3723487Z 
2026-09-14T10:42:00.3723841Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-09-14T10:42:00.3796659Z                     res = fixturedef.cached_result[0]
2026-09-14T10:42:00.3796948Z >                   pickle.dump(res, f)
2026-09-14T10:42:00.3797425Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:42:00.3798088Z 
2026-09-14T10:42:00.3798545Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-09-14T10:42:00.3859794Z                     res = fixturedef.cached_result[0]
2026-09-14T10:42:00.3860086Z >                   pickle.dump(res, f)
2026-09-14T10:42:00.3860554Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:42:00.3860948Z 
2026-09-14T10:42:00.3861281Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-09-14T10:42:00.3919605Z                     res = fixturedef.cached_result[0]
2026-09-14T10:42:00.3919901Z >                   pickle.dump(res, f)
2026-09-14T10:42:00.3920371Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:42:00.3920759Z 
2026-09-14T10:42:00.3921092Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-09-14T10:42:00.3984317Z                     res = fixturedef.cached_result[0]
2026-09-14T10:42:00.3984609Z >                   pickle.dump(res, f)
2026-09-14T10:42:00.3985079Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:42:00.3985479Z 
2026-09-14T10:42:00.3985813Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 11. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 103940541412
- **Started:** 2026-09-14T10:26:43Z
- **Completed:** 2026-09-14T10:43:17Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541412)

#### Error Details

**Error 1:**
```
2026-09-14T10:43:15.0936789Z                     res = fixturedef.cached_result[0]
2026-09-14T10:43:15.0937257Z >                   pickle.dump(res, f)
2026-09-14T10:43:15.0938014Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:43:15.0938641Z 
2026-09-14T10:43:15.0939202Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-09-14T10:43:15.1044841Z                     res = fixturedef.cached_result[0]
2026-09-14T10:43:15.1045325Z >                   pickle.dump(res, f)
2026-09-14T10:43:15.1046123Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:43:15.1046786Z 
2026-09-14T10:43:15.1047356Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-09-14T10:43:15.1139405Z                     res = fixturedef.cached_result[0]
2026-09-14T10:43:15.1139821Z >                   pickle.dump(res, f)
2026-09-14T10:43:15.1140504Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:43:15.1141079Z 
2026-09-14T10:43:15.1141561Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-09-14T10:43:15.1225081Z                     res = fixturedef.cached_result[0]
2026-09-14T10:43:15.1225490Z >                   pickle.dump(res, f)
2026-09-14T10:43:15.1226198Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:43:15.1226764Z 
2026-09-14T10:43:15.1227253Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-09-14T10:43:15.1293209Z                     res = fixturedef.cached_result[0]
2026-09-14T10:43:15.1293497Z >                   pickle.dump(res, f)
2026-09-14T10:43:15.1293964Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-14T10:43:15.1294347Z 
2026-09-14T10:43:15.1294677Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 12. project_cpu_tests_linux (AllenCahn_Bayreuth)

- **Job ID:** 103940541441
- **Started:** 2026-09-14T10:24:47Z
- **Completed:** 2026-09-14T10:25:32Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34833036623/job/103940541441)

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
