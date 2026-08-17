# Automated Test Failure Analysis

**Generated:** 2026-08-17T05:55:00.257086+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/31998529445

## Summary

- Total Jobs: 30
- Failed Jobs: 8

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 95294452520
- **Started:** 2026-08-17T05:37:08Z
- **Completed:** 2026-08-17T05:43:13Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452520)

#### Error Details

**Error 1:**
```
2026-08-17T05:38:37.8815839Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-08-17T05:38:37.8816211Z 
2026-08-17T05:38:40.6530524Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-08-17T05:38:40.6716009Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-08-17T05:38:40.6787005Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-08-17T05:40:44.3018455Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-08-17T05:40:46.0683657Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-17T05:40:46.1181634Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-17T05:40:46.1357518Z ../../
```

**Error 3:**
```
2026-08-17T05:40:46.0683657Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-17T05:40:46.1181634Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-17T05:40:46.1357518Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-17T05:40:46.1534239Z ../../../../reposi
```

**Error 4:**
```
2026-08-17T05:40:46.1181634Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-17T05:40:46.1357518Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-17T05:40:46.1534239Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-17T05:40:46.1720797Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-08-17T05:40:46.1357518Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-17T05:40:46.1534239Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-17T05:40:46.1720797Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-08-17T05:40:46.1911646Z ../../../../repositories/py
```

### 2. project_cpu_tests_linux (DAE)

- **Job ID:** 95294452587
- **Started:** 2026-08-17T05:37:57Z
- **Completed:** 2026-08-17T05:38:36Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452587)

No specific error messages extracted. Check job logs for details.

### 3. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 95294452603
- **Started:** 2026-08-17T05:37:08Z
- **Completed:** 2026-08-17T05:40:22Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452603)

#### Error Details

**Error 1:**
```
2026-08-17T05:38:27.1785537Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-17T05:38:27.2043523Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-17T05:38:27.2919746Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:27.3201598Z pySDC/test
```

**Error 2:**
```
2026-08-17T05:38:27.2043523Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-17T05:38:27.2919746Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:27.3201598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:27.3483026Z pySDC/te
```

**Error 3:**
```
2026-08-17T05:38:27.2919746Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:27.3201598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:27.3483026Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:27.3770252Z pySDC/
```

**Error 4:**
```
2026-08-17T05:38:27.3201598Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:27.3483026Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:27.3770252Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-17T05:38:27.4057196Z pySDC/
```

**Error 5:**
```
2026-08-17T05:38:27.3483026Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:27.3770252Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-17T05:38:27.4057196Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-17T05:38:27.4340001Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 95294452611
- **Started:** 2026-08-17T05:37:08Z
- **Completed:** 2026-08-17T05:40:05Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452611)

#### Error Details

**Error 1:**
```
2026-08-17T05:38:22.3919252Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-17T05:38:22.4218388Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-17T05:38:22.4966723Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:22.5274910Z pySDC/test
```

**Error 2:**
```
2026-08-17T05:38:22.4218388Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-17T05:38:22.4966723Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:22.5274910Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:22.5586220Z pySDC/te
```

**Error 3:**
```
2026-08-17T05:38:22.4966723Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:22.5274910Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:22.5586220Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:22.5892523Z pySDC/
```

**Error 4:**
```
2026-08-17T05:38:22.5274910Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:22.5586220Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:22.5892523Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-17T05:38:22.6195200Z pySDC/
```

**Error 5:**
```
2026-08-17T05:38:22.5586220Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:22.5892523Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-17T05:38:22.6195200Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-17T05:38:22.6541800Z pySDC/tests/
```

### 5. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 95294452617
- **Started:** 2026-08-17T05:37:08Z
- **Completed:** 2026-08-17T05:52:59Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452617)

#### Error Details

**Error 1:**
```
2026-08-17T05:52:57.7149169Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:57.7149649Z >                   pickle.dump(res, f)
2026-08-17T05:52:57.7150444Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:57.7151137Z 
2026-08-17T05:52:57.7151718Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-17T05:52:57.7257352Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:57.7257881Z >                   pickle.dump(res, f)
2026-08-17T05:52:57.7258748Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:57.7259492Z 
2026-08-17T05:52:57.7260122Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-17T05:52:57.7361942Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:57.7362227Z >                   pickle.dump(res, f)
2026-08-17T05:52:57.7362947Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:57.7363358Z 
2026-08-17T05:52:57.7363701Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-17T05:52:57.7423184Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:57.7423468Z >                   pickle.dump(res, f)
2026-08-17T05:52:57.7423937Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:57.7424332Z 
2026-08-17T05:52:57.7424662Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-17T05:52:57.7482347Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:57.7482871Z >                   pickle.dump(res, f)
2026-08-17T05:52:57.7483337Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:57.7483732Z 
2026-08-17T05:52:57.7484069Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 6. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 95294452620
- **Started:** 2026-08-17T05:37:08Z
- **Completed:** 2026-08-17T05:39:34Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452620)

#### Error Details

**Error 1:**
```
2026-08-17T05:38:18.0368837Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-17T05:38:18.0562935Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-17T05:38:18.1351143Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:18.1584071Z pySDC/test
```

**Error 2:**
```
2026-08-17T05:38:18.0562935Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-17T05:38:18.1351143Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:18.1584071Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:18.1810083Z pySDC/te
```

**Error 3:**
```
2026-08-17T05:38:18.1351143Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-17T05:38:18.1584071Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:18.1810083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:18.2039175Z pySDC/
```

**Error 4:**
```
2026-08-17T05:38:18.1584071Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-17T05:38:18.1810083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:18.2039175Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-17T05:38:18.2266575Z pySDC/
```

**Error 5:**
```
2026-08-17T05:38:18.1810083Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-17T05:38:18.2039175Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-17T05:38:18.2266575Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-17T05:38:18.2495497Z pySDC/tests/
```

### 7. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 95294452631
- **Started:** 2026-08-17T05:37:09Z
- **Completed:** 2026-08-17T05:54:15Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452631)

#### Error Details

**Error 1:**
```
2026-08-17T05:54:11.0157535Z                     res = fixturedef.cached_result[0]
2026-08-17T05:54:11.0157828Z >                   pickle.dump(res, f)
2026-08-17T05:54:11.0158290Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:54:11.0158676Z 
2026-08-17T05:54:11.0159014Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-17T05:54:11.0218074Z                     res = fixturedef.cached_result[0]
2026-08-17T05:54:11.0218546Z >                   pickle.dump(res, f)
2026-08-17T05:54:11.0219325Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:54:11.0219986Z 
2026-08-17T05:54:11.0220538Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-17T05:54:11.0296665Z                     res = fixturedef.cached_result[0]
2026-08-17T05:54:11.0297204Z >                   pickle.dump(res, f)
2026-08-17T05:54:11.0297725Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:54:11.0298114Z 
2026-08-17T05:54:11.0298445Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-17T05:54:11.0355606Z                     res = fixturedef.cached_result[0]
2026-08-17T05:54:11.0355888Z >                   pickle.dump(res, f)
2026-08-17T05:54:11.0356351Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:54:11.0356735Z 
2026-08-17T05:54:11.0357178Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-17T05:54:11.0414747Z                     res = fixturedef.cached_result[0]
2026-08-17T05:54:11.0415037Z >                   pickle.dump(res, f)
2026-08-17T05:54:11.0415499Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:54:11.0415888Z 
2026-08-17T05:54:11.0416213Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 8. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 95294452645
- **Started:** 2026-08-17T05:37:08Z
- **Completed:** 2026-08-17T05:52:57Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31998529445/job/95294452645)

#### Error Details

**Error 1:**
```
2026-08-17T05:52:53.0349943Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:53.0350354Z >                   pickle.dump(res, f)
2026-08-17T05:52:53.0350838Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:53.0351233Z 
2026-08-17T05:52:53.0351571Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-17T05:52:53.0415684Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:53.0415974Z >                   pickle.dump(res, f)
2026-08-17T05:52:53.0416662Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:53.0417069Z 
2026-08-17T05:52:53.0417419Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-17T05:52:53.0484949Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:53.0485231Z >                   pickle.dump(res, f)
2026-08-17T05:52:53.0485708Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:53.0486097Z 
2026-08-17T05:52:53.0486540Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-17T05:52:53.0543436Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:53.0543721Z >                   pickle.dump(res, f)
2026-08-17T05:52:53.0544201Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:53.0544592Z 
2026-08-17T05:52:53.0544925Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-17T05:52:53.0601254Z                     res = fixturedef.cached_result[0]
2026-08-17T05:52:53.0601534Z >                   pickle.dump(res, f)
2026-08-17T05:52:53.0602009Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-17T05:52:53.0602398Z 
2026-08-17T05:52:53.0602730Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
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
