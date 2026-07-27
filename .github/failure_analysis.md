# Automated Test Failure Analysis

**Generated:** 2026-07-27T08:55:00.045430+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/30250364635

## Summary

- Total Jobs: 30
- Failed Jobs: 6

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 89926747027
- **Started:** 2026-07-27T08:33:39Z
- **Completed:** 2026-07-27T08:41:02Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30250364635/job/89926747027)

#### Error Details

**Error 1:**
```
2026-07-27T08:35:06.5222488Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-07-27T08:35:06.5222961Z 
2026-07-27T08:35:09.9527836Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-07-27T08:35:09.9763125Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-07-27T08:35:09.9861769Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-07-27T08:37:51.5349706Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-07-27T08:37:53.6618888Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-27T08:37:53.7241565Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-27T08:37:53.7487473Z ../../
```

**Error 3:**
```
2026-07-27T08:37:53.6618888Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-27T08:37:53.7241565Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-27T08:37:53.7487473Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-27T08:37:53.7727316Z ../../../../reposi
```

**Error 4:**
```
2026-07-27T08:37:53.7241565Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-27T08:37:53.7487473Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-27T08:37:53.7727316Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-27T08:37:53.7977336Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-07-27T08:37:53.7487473Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-27T08:37:53.7727316Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-27T08:37:53.7977336Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-07-27T08:37:53.8232484Z ../../../../repositories/py
```

### 2. project_cpu_tests_linux (SDC_showdown)

- **Job ID:** 89926747044
- **Started:** 2026-07-27T08:33:39Z
- **Completed:** 2026-07-27T08:37:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30250364635/job/89926747044)

No specific error messages extracted. Check job logs for details.

### 3. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 89926747090
- **Started:** 2026-07-27T08:33:39Z
- **Completed:** 2026-07-27T08:36:18Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30250364635/job/89926747090)

#### Error Details

**Error 1:**
```
2026-07-27T08:34:50.1838687Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-27T08:34:50.2104710Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-27T08:34:50.2856045Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-27T08:34:50.3141415Z pySDC/test
```

**Error 2:**
```
2026-07-27T08:34:50.2104710Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-27T08:34:50.2856045Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-27T08:34:50.3141415Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-27T08:34:50.3423035Z pySDC/te
```

**Error 3:**
```
2026-07-27T08:34:50.2856045Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-27T08:34:50.3141415Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-27T08:34:50.3423035Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-27T08:34:50.3707327Z pySDC/
```

**Error 4:**
```
2026-07-27T08:34:50.3141415Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-27T08:34:50.3423035Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-27T08:34:50.3707327Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-27T08:34:50.3988705Z pySDC/
```

**Error 5:**
```
2026-07-27T08:34:50.3423035Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-27T08:34:50.3707327Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-27T08:34:50.3988705Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-27T08:34:50.4282843Z pySDC/tests/
```

### 4. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 89926747106
- **Started:** 2026-07-27T08:34:30Z
- **Completed:** 2026-07-27T08:50:02Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30250364635/job/89926747106)

#### Error Details

**Error 1:**
```
2026-07-27T08:49:59.2762430Z                     res = fixturedef.cached_result[0]
2026-07-27T08:49:59.2762710Z >                   pickle.dump(res, f)
2026-07-27T08:49:59.2763188Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-27T08:49:59.2763595Z 
2026-07-27T08:49:59.2763936Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-07-27T08:49:59.2834333Z                     res = fixturedef.cached_result[0]
2026-07-27T08:49:59.2834827Z >                   pickle.dump(res, f)
2026-07-27T08:49:59.2835681Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-27T08:49:59.2836426Z 
2026-07-27T08:49:59.2837019Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-07-27T08:49:59.2913950Z                     res = fixturedef.cached_result[0]
2026-07-27T08:49:59.2914230Z >                   pickle.dump(res, f)
2026-07-27T08:49:59.2914702Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-27T08:49:59.2915101Z 
2026-07-27T08:49:59.2915434Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-07-27T08:49:59.2974064Z                     res = fixturedef.cached_result[0]
2026-07-27T08:49:59.2974473Z >                   pickle.dump(res, f)
2026-07-27T08:49:59.2974953Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-27T08:49:59.2975363Z 
2026-07-27T08:49:59.2975691Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-07-27T08:49:59.3033528Z                     res = fixturedef.cached_result[0]
2026-07-27T08:49:59.3033810Z >                   pickle.dump(res, f)
2026-07-27T08:49:59.3034285Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-07-27T08:49:59.3034696Z 
2026-07-27T08:49:59.3035032Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 5. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 89926747113
- **Started:** 2026-07-27T08:33:39Z
- **Completed:** 2026-07-27T08:36:41Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30250364635/job/89926747113)

#### Error Details

**Error 1:**
```
2026-07-27T08:34:57.6155163Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-27T08:34:57.6421074Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-27T08:34:57.7408042Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-27T08:34:57.7698067Z pySDC/test
```

**Error 2:**
```
2026-07-27T08:34:57.6421074Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-27T08:34:57.7408042Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-27T08:34:57.7698067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-27T08:34:57.7989736Z pySDC/te
```

**Error 3:**
```
2026-07-27T08:34:57.7408042Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-27T08:34:57.7698067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-27T08:34:57.7989736Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-27T08:34:57.8286079Z pySDC/
```

**Error 4:**
```
2026-07-27T08:34:57.7698067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-27T08:34:57.7989736Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-27T08:34:57.8286079Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-27T08:34:57.8584437Z pySDC/
```

**Error 5:**
```
2026-07-27T08:34:57.7989736Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-27T08:34:57.8286079Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-27T08:34:57.8584437Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-27T08:34:57.8882302Z pySDC/tests/
```

### 6. user_cpu_tests_linux (petsc, 3.11)

- **Job ID:** 89926747147
- **Started:** 2026-07-27T08:34:32Z
- **Completed:** 2026-07-27T08:35:34Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/30250364635/job/89926747147)

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
