# Automated Test Failure Analysis

**Generated:** 2026-08-31T11:45:28.929648+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/33387005475

## Summary

- Total Jobs: 30
- Failed Jobs: 12

## Failed Jobs

### 1. user_cpu_tests_linux (petsc, 3.10)

- **Job ID:** 99471777543
- **Started:** 2026-08-31T11:27:01Z
- **Completed:** 2026-08-31T11:27:50Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777543)

No specific error messages extracted. Check job logs for details.

### 2. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 99471777555
- **Started:** 2026-08-31T11:27:01Z
- **Completed:** 2026-08-31T11:44:12Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777555)

#### Error Details

**Error 1:**
```
2026-08-31T11:43:39.2808442Z                     res = fixturedef.cached_result[0]
2026-08-31T11:43:39.2808938Z >                   pickle.dump(res, f)
2026-08-31T11:43:39.2809801Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:43:39.2810798Z 
2026-08-31T11:43:39.2811422Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-31T11:43:39.2926955Z                     res = fixturedef.cached_result[0]
2026-08-31T11:43:39.2927470Z >                   pickle.dump(res, f)
2026-08-31T11:43:39.2928345Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:43:39.2929113Z 
2026-08-31T11:43:39.2929736Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-31T11:43:39.3023277Z                     res = fixturedef.cached_result[0]
2026-08-31T11:43:39.3023738Z >                   pickle.dump(res, f)
2026-08-31T11:43:39.3024490Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:43:39.3025149Z 
2026-08-31T11:43:39.3025676Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-31T11:43:39.3106670Z                     res = fixturedef.cached_result[0]
2026-08-31T11:43:39.3106958Z >                   pickle.dump(res, f)
2026-08-31T11:43:39.3107446Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:43:39.3107852Z 
2026-08-31T11:43:39.3108188Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-31T11:43:39.3171491Z                     res = fixturedef.cached_result[0]
2026-08-31T11:43:39.3171775Z >                   pickle.dump(res, f)
2026-08-31T11:43:39.3172250Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:43:39.3172660Z 
2026-08-31T11:43:39.3172983Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 3. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 99471777559
- **Started:** 2026-08-31T11:27:02Z
- **Completed:** 2026-08-31T11:29:05Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777559)

#### Error Details

**Error 1:**
```
2026-08-31T11:28:06.5408567Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-31T11:28:06.5540936Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-31T11:28:06.6174360Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:06.6390560Z pySDC/test
```

**Error 2:**
```
2026-08-31T11:28:06.5540936Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-31T11:28:06.6174360Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:06.6390560Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:06.6556734Z pySDC/te
```

**Error 3:**
```
2026-08-31T11:28:06.6174360Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:06.6390560Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:06.6556734Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:06.6714900Z pySDC/
```

**Error 4:**
```
2026-08-31T11:28:06.6390560Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:06.6556734Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:06.6714900Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-31T11:28:06.6879104Z pySDC/
```

**Error 5:**
```
2026-08-31T11:28:06.6556734Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:06.6714900Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-31T11:28:06.6879104Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-31T11:28:06.7052638Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 99471777604
- **Started:** 2026-08-31T11:27:01Z
- **Completed:** 2026-08-31T11:29:50Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777604)

#### Error Details

**Error 1:**
```
2026-08-31T11:28:18.6598877Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-31T11:28:18.6841250Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-31T11:28:18.7763720Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:18.8050008Z pySDC/test
```

**Error 2:**
```
2026-08-31T11:28:18.6841250Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-31T11:28:18.7763720Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:18.8050008Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:18.8333091Z pySDC/te
```

**Error 3:**
```
2026-08-31T11:28:18.7763720Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:18.8050008Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:18.8333091Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:18.8614595Z pySDC/
```

**Error 4:**
```
2026-08-31T11:28:18.8050008Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:18.8333091Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:18.8614595Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-31T11:28:18.8906800Z pySDC/
```

**Error 5:**
```
2026-08-31T11:28:18.8333091Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:18.8614595Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-31T11:28:18.8906800Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-31T11:28:18.9194946Z pySDC/tests/
```

### 5. user_firedrake_tests

- **Job ID:** 99471777609
- **Started:** 2026-08-31T11:27:01Z
- **Completed:** 2026-08-31T11:34:22Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777609)

#### Error Details

**Error 1:**
```
2026-08-31T11:28:25.3313045Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-08-31T11:28:25.3313693Z 
2026-08-31T11:28:28.7799089Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-08-31T11:28:28.8025458Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-08-31T11:28:28.8117237Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-08-31T11:31:10.3683141Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-08-31T11:31:14.2007980Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-31T11:31:14.2618958Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-31T11:31:14.2854114Z ../../
```

**Error 3:**
```
2026-08-31T11:31:14.2007980Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-31T11:31:14.2618958Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-31T11:31:14.2854114Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-31T11:31:14.3076889Z ../../../../reposi
```

**Error 4:**
```
2026-08-31T11:31:14.2618958Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-31T11:31:14.2854114Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-31T11:31:14.3076889Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-31T11:31:14.3312688Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-08-31T11:31:14.2854114Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-31T11:31:14.3076889Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-31T11:31:14.3312688Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-08-31T11:31:14.3552677Z ../../../../repositories/py
```

### 6. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 99471777644
- **Started:** 2026-08-31T11:27:02Z
- **Completed:** 2026-08-31T11:41:48Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777644)

#### Error Details

**Error 1:**
```
2026-08-31T11:41:45.7664620Z                     res = fixturedef.cached_result[0]
2026-08-31T11:41:45.7664972Z >                   pickle.dump(res, f)
2026-08-31T11:41:45.7665544Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:41:45.7666013Z 
2026-08-31T11:41:45.7666434Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-31T11:41:45.7743328Z                     res = fixturedef.cached_result[0]
2026-08-31T11:41:45.7743718Z >                   pickle.dump(res, f)
2026-08-31T11:41:45.7744340Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:41:45.7744852Z 
2026-08-31T11:41:45.7745300Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-31T11:41:45.7818973Z                     res = fixturedef.cached_result[0]
2026-08-31T11:41:45.7819302Z >                   pickle.dump(res, f)
2026-08-31T11:41:45.7819822Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:41:45.7820269Z 
2026-08-31T11:41:45.7820651Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-31T11:41:45.7880663Z                     res = fixturedef.cached_result[0]
2026-08-31T11:41:45.7880891Z >                   pickle.dump(res, f)
2026-08-31T11:41:45.7881264Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:41:45.7881558Z 
2026-08-31T11:41:45.7881819Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-31T11:41:45.7926226Z                     res = fixturedef.cached_result[0]
2026-08-31T11:41:45.7926459Z >                   pickle.dump(res, f)
2026-08-31T11:41:45.7926828Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:41:45.7927123Z 
2026-08-31T11:41:45.7927384Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 7. user_cpu_tests_linux (pytorch, 3.13)

- **Job ID:** 99471777657
- **Started:** 2026-08-31T11:27:02Z
- **Completed:** 2026-08-31T11:28:07Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777657)

No specific error messages extracted. Check job logs for details.

### 8. user_cpu_tests_linux (pytorch, 3.11)

- **Job ID:** 99471777660
- **Started:** 2026-08-31T11:27:01Z
- **Completed:** 2026-08-31T11:28:06Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777660)

No specific error messages extracted. Check job logs for details.

### 9. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 99471777699
- **Started:** 2026-08-31T11:27:56Z
- **Completed:** 2026-08-31T11:44:03Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777699)

#### Error Details

**Error 1:**
```
2026-08-31T11:44:01.1974637Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:01.1975043Z >                   pickle.dump(res, f)
2026-08-31T11:44:01.1975538Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:01.1975954Z 
2026-08-31T11:44:01.1976304Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-31T11:44:01.2054392Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:01.2054682Z >                   pickle.dump(res, f)
2026-08-31T11:44:01.2055177Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:01.2055580Z 
2026-08-31T11:44:01.2055918Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-31T11:44:01.2115338Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:01.2115627Z >                   pickle.dump(res, f)
2026-08-31T11:44:01.2116108Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:01.2116511Z 
2026-08-31T11:44:01.2116845Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-31T11:44:01.2180427Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:01.2180713Z >                   pickle.dump(res, f)
2026-08-31T11:44:01.2181205Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:01.2181736Z 
2026-08-31T11:44:01.2182069Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-31T11:44:01.2245577Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:01.2246125Z >                   pickle.dump(res, f)
2026-08-31T11:44:01.2246991Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:01.2247717Z 
2026-08-31T11:44:01.2248061Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 10. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 99471777749
- **Started:** 2026-08-31T11:27:01Z
- **Completed:** 2026-08-31T11:29:42Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777749)

#### Error Details

**Error 1:**
```
2026-08-31T11:28:14.1283317Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-31T11:28:14.1547477Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-31T11:28:14.2297084Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:14.2579163Z pySDC/test
```

**Error 2:**
```
2026-08-31T11:28:14.1547477Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-31T11:28:14.2297084Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:14.2579163Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:14.2859133Z pySDC/te
```

**Error 3:**
```
2026-08-31T11:28:14.2297084Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-31T11:28:14.2579163Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:14.2859133Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:14.3137704Z pySDC/
```

**Error 4:**
```
2026-08-31T11:28:14.2579163Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-31T11:28:14.2859133Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:14.3137704Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-31T11:28:14.3415446Z pySDC/
```

**Error 5:**
```
2026-08-31T11:28:14.2859133Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-31T11:28:14.3137704Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-31T11:28:14.3415446Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-31T11:28:14.3701384Z pySDC/tests/
```

### 11. project_cpu_tests_linux (DAE)

- **Job ID:** 99471777786
- **Started:** 2026-08-31T11:27:02Z
- **Completed:** 2026-08-31T11:27:46Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777786)

No specific error messages extracted. Check job logs for details.

### 12. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 99471777816
- **Started:** 2026-08-31T11:27:57Z
- **Completed:** 2026-08-31T11:44:44Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/33387005475/job/99471777816)

#### Error Details

**Error 1:**
```
2026-08-31T11:44:41.3480323Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:41.3480839Z >                   pickle.dump(res, f)
2026-08-31T11:44:41.3481691Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:41.3482424Z 
2026-08-31T11:44:41.3483038Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-31T11:44:41.3565213Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:41.3565903Z >                   pickle.dump(res, f)
2026-08-31T11:44:41.3566513Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:41.3566909Z 
2026-08-31T11:44:41.3567250Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-31T11:44:41.3628860Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:41.3629157Z >                   pickle.dump(res, f)
2026-08-31T11:44:41.3629758Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:41.3630160Z 
2026-08-31T11:44:41.3630499Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-31T11:44:41.3689890Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:41.3690185Z >                   pickle.dump(res, f)
2026-08-31T11:44:41.3690668Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:41.3691068Z 
2026-08-31T11:44:41.3691402Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-31T11:44:41.3751366Z                     res = fixturedef.cached_result[0]
2026-08-31T11:44:41.3751665Z >                   pickle.dump(res, f)
2026-08-31T11:44:41.3752147Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-31T11:44:41.3752547Z 
2026-08-31T11:44:41.3752879Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
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
