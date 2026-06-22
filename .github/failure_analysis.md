# Automated Test Failure Analysis

**Generated:** 2026-06-22T10:57:28.034440+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/27946980556

## Summary

- Total Jobs: 30
- Failed Jobs: 6

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 82694118216
- **Started:** 2026-06-22T10:42:32Z
- **Completed:** 2026-06-22T10:49:33Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27946980556/job/82694118216)

#### Error Details

**Error 1:**
```
2026-06-22T10:43:57.1308983Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-06-22T10:43:57.1309467Z 
2026-06-22T10:44:00.3545167Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-06-22T10:44:00.3764834Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-06-22T10:44:00.3853794Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-06-22T10:46:30.3458553Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-06-22T10:46:34.4135489Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-22T10:46:34.4769610Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-22T10:46:34.5006468Z ../../
```

**Error 3:**
```
2026-06-22T10:46:34.4135489Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-22T10:46:34.4769610Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-22T10:46:34.5006468Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-22T10:46:34.5237160Z ../../../../reposi
```

**Error 4:**
```
2026-06-22T10:46:34.4769610Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-22T10:46:34.5006468Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-22T10:46:34.5237160Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-22T10:46:34.5483704Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-06-22T10:46:34.5006468Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-22T10:46:34.5237160Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-22T10:46:34.5483704Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-06-22T10:46:34.5726846Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 82694118398
- **Started:** 2026-06-22T10:42:32Z
- **Completed:** 2026-06-22T10:45:30Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27946980556/job/82694118398)

#### Error Details

**Error 1:**
```
2026-06-22T10:43:46.3932470Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-22T10:43:46.4199005Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-22T10:43:46.5205264Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-22T10:43:46.5522171Z pySDC/test
```

**Error 2:**
```
2026-06-22T10:43:46.4199005Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-22T10:43:46.5205264Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-22T10:43:46.5522171Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-22T10:43:46.5829335Z pySDC/te
```

**Error 3:**
```
2026-06-22T10:43:46.5205264Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-22T10:43:46.5522171Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-22T10:43:46.5829335Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-22T10:43:46.6147433Z pySDC/
```

**Error 4:**
```
2026-06-22T10:43:46.5522171Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-22T10:43:46.5829335Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-22T10:43:46.6147433Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-22T10:43:46.6456022Z pySDC/
```

**Error 5:**
```
2026-06-22T10:43:46.5829335Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-22T10:43:46.6147433Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-22T10:43:46.6456022Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-22T10:43:46.6769100Z pySDC/tests/
```

### 3. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 82694118443
- **Started:** 2026-06-22T10:42:33Z
- **Completed:** 2026-06-22T10:53:47Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27946980556/job/82694118443)

#### Error Details

**Error 1:**
```
2026-06-22T10:53:45.1115029Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:45.1115350Z >                   pickle.dump(res, f)
2026-06-22T10:53:45.1115885Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:45.1116322Z 
2026-06-22T10:53:45.1116702Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-06-22T10:53:45.1188140Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:45.1188830Z >                   pickle.dump(res, f)
2026-06-22T10:53:45.1189644Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:45.1190334Z 
2026-06-22T10:53:45.1190946Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-06-22T10:53:45.1271761Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:45.1272053Z >                   pickle.dump(res, f)
2026-06-22T10:53:45.1272524Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:45.1272914Z 
2026-06-22T10:53:45.1273245Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-06-22T10:53:45.1331689Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:45.1331973Z >                   pickle.dump(res, f)
2026-06-22T10:53:45.1332439Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:45.1332833Z 
2026-06-22T10:53:45.1333163Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-06-22T10:53:45.1391508Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:45.1391791Z >                   pickle.dump(res, f)
2026-06-22T10:53:45.1392259Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:45.1392653Z 
2026-06-22T10:53:45.1392978Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 4. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 82694118452
- **Started:** 2026-06-22T10:42:33Z
- **Completed:** 2026-06-22T10:54:02Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27946980556/job/82694118452)

#### Error Details

**Error 1:**
```
2026-06-22T10:53:59.2615930Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:59.2616449Z >                   pickle.dump(res, f)
2026-06-22T10:53:59.2617504Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:59.2618285Z 
2026-06-22T10:53:59.2618920Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-06-22T10:53:59.2727109Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:59.2727637Z >                   pickle.dump(res, f)
2026-06-22T10:53:59.2728749Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:59.2729521Z 
2026-06-22T10:53:59.2730138Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-06-22T10:53:59.2822128Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:59.2822411Z >                   pickle.dump(res, f)
2026-06-22T10:53:59.2822889Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:59.2823291Z 
2026-06-22T10:53:59.2823625Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-06-22T10:53:59.2881739Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:59.2882033Z >                   pickle.dump(res, f)
2026-06-22T10:53:59.2882519Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:59.2882922Z 
2026-06-22T10:53:59.2883258Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-06-22T10:53:59.2942222Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:59.2942509Z >                   pickle.dump(res, f)
2026-06-22T10:53:59.2942990Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:59.2943401Z 
2026-06-22T10:53:59.2943734Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 5. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 82694118470
- **Started:** 2026-06-22T10:43:33Z
- **Completed:** 2026-06-22T10:55:59Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27946980556/job/82694118470)

#### Error Details

**Error 1:**
```
2026-06-22T10:55:55.1122767Z                     res = fixturedef.cached_result[0]
2026-06-22T10:55:55.1123282Z >                   pickle.dump(res, f)
2026-06-22T10:55:55.1124032Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:55:55.1124472Z 
2026-06-22T10:55:55.1124839Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-06-22T10:55:55.1185169Z                     res = fixturedef.cached_result[0]
2026-06-22T10:55:55.1185453Z >                   pickle.dump(res, f)
2026-06-22T10:55:55.1186079Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:55:55.1186474Z 
2026-06-22T10:55:55.1186801Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-06-22T10:55:55.1259154Z                     res = fixturedef.cached_result[0]
2026-06-22T10:55:55.1259440Z >                   pickle.dump(res, f)
2026-06-22T10:55:55.1259902Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:55:55.1260296Z 
2026-06-22T10:55:55.1260622Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-06-22T10:55:55.1318321Z                     res = fixturedef.cached_result[0]
2026-06-22T10:55:55.1318605Z >                   pickle.dump(res, f)
2026-06-22T10:55:55.1319070Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:55:55.1319462Z 
2026-06-22T10:55:55.1319792Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-06-22T10:55:55.1378611Z                     res = fixturedef.cached_result[0]
2026-06-22T10:55:55.1378895Z >                   pickle.dump(res, f)
2026-06-22T10:55:55.1379360Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:55:55.1379753Z 
2026-06-22T10:55:55.1380078Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 6. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 82694118471
- **Started:** 2026-06-22T10:42:33Z
- **Completed:** 2026-06-22T10:53:09Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27946980556/job/82694118471)

#### Error Details

**Error 1:**
```
2026-06-22T10:53:07.0323791Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:07.0324094Z >                   pickle.dump(res, f)
2026-06-22T10:53:07.0324603Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:07.0325008Z 
2026-06-22T10:53:07.0325369Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-06-22T10:53:07.0398259Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:07.0398567Z >                   pickle.dump(res, f)
2026-06-22T10:53:07.0399056Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:07.0399447Z 
2026-06-22T10:53:07.0399789Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-06-22T10:53:07.0470856Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:07.0471153Z >                   pickle.dump(res, f)
2026-06-22T10:53:07.0471643Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:07.0472036Z 
2026-06-22T10:53:07.0472363Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-06-22T10:53:07.0530235Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:07.0530537Z >                   pickle.dump(res, f)
2026-06-22T10:53:07.0531022Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:07.0531413Z 
2026-06-22T10:53:07.0531752Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-06-22T10:53:07.0590334Z                     res = fixturedef.cached_result[0]
2026-06-22T10:53:07.0590641Z >                   pickle.dump(res, f)
2026-06-22T10:53:07.0591123Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-06-22T10:53:07.0591524Z 
2026-06-22T10:53:07.0591858Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
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
