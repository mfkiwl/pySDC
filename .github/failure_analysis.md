# Automated Test Failure Analysis

**Generated:** 2026-08-10T06:33:39.762467+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/31361078390

## Summary

- Total Jobs: 30
- Failed Jobs: 6

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 93369939546
- **Started:** 2026-08-10T06:12:01Z
- **Completed:** 2026-08-10T06:19:03Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31361078390/job/93369939546)

#### Error Details

**Error 1:**
```
2026-08-10T06:13:25.8750047Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-08-10T06:13:25.8750806Z 
2026-08-10T06:13:29.1504072Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-08-10T06:13:29.1738348Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-08-10T06:13:29.1834651Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-08-10T06:16:00.7779056Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-08-10T06:16:03.0269046Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-10T06:16:03.0920790Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-10T06:16:03.1159538Z ../../
```

**Error 3:**
```
2026-08-10T06:16:03.0269046Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-10T06:16:03.0920790Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-10T06:16:03.1159538Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-10T06:16:03.1393317Z ../../../../reposi
```

**Error 4:**
```
2026-08-10T06:16:03.0920790Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-10T06:16:03.1159538Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-10T06:16:03.1393317Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-10T06:16:03.1637759Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-08-10T06:16:03.1159538Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-10T06:16:03.1393317Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-10T06:16:03.1637759Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-08-10T06:16:03.1886622Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 93369939700
- **Started:** 2026-08-10T06:15:10Z
- **Completed:** 2026-08-10T06:30:46Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31361078390/job/93369939700)

#### Error Details

**Error 1:**
```
2026-08-10T06:30:44.5791931Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:44.5792397Z >                   pickle.dump(res, f)
2026-08-10T06:30:44.5793140Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:44.5793762Z 
2026-08-10T06:30:44.5794290Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-10T06:30:44.5864449Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:44.5864885Z >                   pickle.dump(res, f)
2026-08-10T06:30:44.5865775Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:44.5866397Z 
2026-08-10T06:30:44.5866918Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-10T06:30:44.5944104Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:44.5944385Z >                   pickle.dump(res, f)
2026-08-10T06:30:44.5944853Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:44.5945534Z 
2026-08-10T06:30:44.5945860Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-10T06:30:44.6001997Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:44.6002288Z >                   pickle.dump(res, f)
2026-08-10T06:30:44.6002757Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:44.6003282Z 
2026-08-10T06:30:44.6003605Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-10T06:30:44.6058830Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:44.6059109Z >                   pickle.dump(res, f)
2026-08-10T06:30:44.6059565Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:44.6059949Z 
2026-08-10T06:30:44.6060267Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 3. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 93369939721
- **Started:** 2026-08-10T06:12:02Z
- **Completed:** 2026-08-10T06:15:34Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31361078390/job/93369939721)

#### Error Details

**Error 1:**
```
2026-08-10T06:13:47.3501482Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-10T06:13:47.3771810Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-10T06:13:47.4780375Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-10T06:13:47.5087640Z pySDC/test
```

**Error 2:**
```
2026-08-10T06:13:47.3771810Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-10T06:13:47.4780375Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-10T06:13:47.5087640Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-10T06:13:47.5390986Z pySDC/te
```

**Error 3:**
```
2026-08-10T06:13:47.4780375Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-10T06:13:47.5087640Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-10T06:13:47.5390986Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-10T06:13:47.5696561Z pySDC/
```

**Error 4:**
```
2026-08-10T06:13:47.5087640Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-10T06:13:47.5390986Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-10T06:13:47.5696561Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-10T06:13:47.5991812Z pySDC/
```

**Error 5:**
```
2026-08-10T06:13:47.5390986Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-10T06:13:47.5696561Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-10T06:13:47.5991812Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-10T06:13:47.6296922Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 93369939724
- **Started:** 2026-08-10T06:14:16Z
- **Completed:** 2026-08-10T06:16:45Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31361078390/job/93369939724)

#### Error Details

**Error 1:**
```
2026-08-10T06:15:35.3831190Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-10T06:15:35.4027599Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-10T06:15:35.4437578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-10T06:15:35.4622821Z pySDC/test
```

**Error 2:**
```
2026-08-10T06:15:35.4027599Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-10T06:15:35.4437578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-10T06:15:35.4622821Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-10T06:15:35.4803583Z pySDC/te
```

**Error 3:**
```
2026-08-10T06:15:35.4437578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-10T06:15:35.4622821Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-10T06:15:35.4803583Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-10T06:15:35.4986009Z pySDC/
```

**Error 4:**
```
2026-08-10T06:15:35.4622821Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-10T06:15:35.4803583Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-10T06:15:35.4986009Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-10T06:15:35.5165849Z pySDC/
```

**Error 5:**
```
2026-08-10T06:15:35.4803583Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-10T06:15:35.4986009Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-10T06:15:35.5165849Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-10T06:15:35.5355278Z pySDC/tests/
```

### 5. user_cpu_tests_linux (pytorch, 3.12)

- **Job ID:** 93369939749
- **Started:** 2026-08-10T06:13:57Z
- **Completed:** 2026-08-10T06:15:04Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31361078390/job/93369939749)

No specific error messages extracted. Check job logs for details.

### 6. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 93369939754
- **Started:** 2026-08-10T06:13:32Z
- **Completed:** 2026-08-10T06:30:35Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/31361078390/job/93369939754)

#### Error Details

**Error 1:**
```
2026-08-10T06:30:33.8744850Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:33.8745236Z >                   pickle.dump(res, f)
2026-08-10T06:30:33.8746148Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:33.8746866Z 
2026-08-10T06:30:33.8747319Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-10T06:30:33.8810894Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:33.8811177Z >                   pickle.dump(res, f)
2026-08-10T06:30:33.8811662Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:33.8812304Z 
2026-08-10T06:30:33.8812794Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-10T06:30:33.8880745Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:33.8881033Z >                   pickle.dump(res, f)
2026-08-10T06:30:33.8881523Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:33.8881940Z 
2026-08-10T06:30:33.8882269Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-10T06:30:33.8940636Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:33.8940922Z >                   pickle.dump(res, f)
2026-08-10T06:30:33.8941407Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:33.8941814Z 
2026-08-10T06:30:33.8942139Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-10T06:30:33.9000521Z                     res = fixturedef.cached_result[0]
2026-08-10T06:30:33.9000807Z >                   pickle.dump(res, f)
2026-08-10T06:30:33.9001296Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-10T06:30:33.9001705Z 
2026-08-10T06:30:33.9002040Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
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
