# Automated Test Failure Analysis

**Generated:** 2026-08-03T08:57:11.138037+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/30797721843

## Summary

- Total Jobs: 30
- Failed Jobs: 4

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 91635007750
- **Started:** 2026-08-03T08:31:33Z
- **Completed:** 2026-08-03T08:38:24Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30797721843/job/91635007750)

#### Error Details

**Error 1:**
```
2026-08-03T08:34:30.0168330Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-08-03T08:34:30.0168788Z 
2026-08-03T08:34:32.4948964Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-08-03T08:34:32.5111078Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-08-03T08:34:32.5171639Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-08-03T08:36:17.8590229Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-08-03T08:36:19.2684314Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-03T08:36:19.3048594Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-03T08:36:19.3203899Z ../../
```

**Error 3:**
```
2026-08-03T08:36:19.2684314Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-08-03T08:36:19.3048594Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-03T08:36:19.3203899Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-03T08:36:19.3356936Z ../../../../reposi
```

**Error 4:**
```
2026-08-03T08:36:19.3048594Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-08-03T08:36:19.3203899Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-03T08:36:19.3356936Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-03T08:36:19.3518189Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-08-03T08:36:19.3203899Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-08-03T08:36:19.3356936Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-08-03T08:36:19.3518189Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-08-03T08:36:19.3680660Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 91635007896
- **Started:** 2026-08-03T08:32:26Z
- **Completed:** 2026-08-03T08:35:57Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30797721843/job/91635007896)

#### Error Details

**Error 1:**
```
2026-08-03T08:34:13.1971059Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-08-03T08:34:13.2234996Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-03T08:34:13.3194955Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-03T08:34:13.3491246Z pySDC/test
```

**Error 2:**
```
2026-08-03T08:34:13.2234996Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-08-03T08:34:13.3194955Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-03T08:34:13.3491246Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-03T08:34:13.3830903Z pySDC/te
```

**Error 3:**
```
2026-08-03T08:34:13.3194955Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-08-03T08:34:13.3491246Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-03T08:34:13.3830903Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-03T08:34:13.4127067Z pySDC/
```

**Error 4:**
```
2026-08-03T08:34:13.3491246Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-08-03T08:34:13.3830903Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-03T08:34:13.4127067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-03T08:34:13.4416797Z pySDC/
```

**Error 5:**
```
2026-08-03T08:34:13.3830903Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-08-03T08:34:13.4127067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-08-03T08:34:13.4416797Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-08-03T08:34:13.4714177Z pySDC/tests/
```

### 3. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 91635007897
- **Started:** 2026-08-03T08:31:39Z
- **Completed:** 2026-08-03T08:48:33Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30797721843/job/91635007897)

#### Error Details

**Error 1:**
```
2026-08-03T08:48:30.4478034Z                     res = fixturedef.cached_result[0]
2026-08-03T08:48:30.4478328Z >                   pickle.dump(res, f)
2026-08-03T08:48:30.4478805Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:48:30.4479202Z 
2026-08-03T08:48:30.4479545Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-03T08:48:30.4547633Z                     res = fixturedef.cached_result[0]
2026-08-03T08:48:30.4548076Z >                   pickle.dump(res, f)
2026-08-03T08:48:30.4548819Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:48:30.4549456Z 
2026-08-03T08:48:30.4549989Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-03T08:48:30.4627316Z                     res = fixturedef.cached_result[0]
2026-08-03T08:48:30.4627608Z >                   pickle.dump(res, f)
2026-08-03T08:48:30.4628077Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:48:30.4628458Z 
2026-08-03T08:48:30.4628793Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-03T08:48:30.4685342Z                     res = fixturedef.cached_result[0]
2026-08-03T08:48:30.4685627Z >                   pickle.dump(res, f)
2026-08-03T08:48:30.4686090Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:48:30.4686463Z 
2026-08-03T08:48:30.4686789Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-03T08:48:30.4743301Z                     res = fixturedef.cached_result[0]
2026-08-03T08:48:30.4743588Z >                   pickle.dump(res, f)
2026-08-03T08:48:30.4744058Z E                   AttributeError: Can't get local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:48:30.4744439Z 
2026-08-03T08:48:30.4744763Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 4. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 91635007898
- **Started:** 2026-08-03T08:32:35Z
- **Completed:** 2026-08-03T08:49:16Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30797721843/job/91635007898)

#### Error Details

**Error 1:**
```
2026-08-03T08:49:13.6649694Z                     res = fixturedef.cached_result[0]
2026-08-03T08:49:13.6650182Z >                   pickle.dump(res, f)
2026-08-03T08:49:13.6651057Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:49:13.6651814Z 
2026-08-03T08:49:13.6652408Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-08-03T08:49:13.6758166Z                     res = fixturedef.cached_result[0]
2026-08-03T08:49:13.6758679Z >                   pickle.dump(res, f)
2026-08-03T08:49:13.6759754Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:49:13.6760513Z 
2026-08-03T08:49:13.6761140Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-08-03T08:49:13.6868659Z                     res = fixturedef.cached_result[0]
2026-08-03T08:49:13.6869232Z >                   pickle.dump(res, f)
2026-08-03T08:49:13.6869877Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:49:13.6870432Z 
2026-08-03T08:49:13.6870879Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-08-03T08:49:13.6930673Z                     res = fixturedef.cached_result[0]
2026-08-03T08:49:13.6930952Z >                   pickle.dump(res, f)
2026-08-03T08:49:13.6931431Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:49:13.6931833Z 
2026-08-03T08:49:13.6932157Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-08-03T08:49:13.6989485Z                     res = fixturedef.cached_result[0]
2026-08-03T08:49:13.6989766Z >                   pickle.dump(res, f)
2026-08-03T08:49:13.6990244Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-08-03T08:49:13.6990639Z 
2026-08-03T08:49:13.6990967Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
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
