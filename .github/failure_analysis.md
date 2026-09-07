# Automated Test Failure Analysis

**Generated:** 2026-09-07T10:21:56.194994+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/34109133973

## Summary

- Total Jobs: 30
- Failed Jobs: 7

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 101701026204
- **Started:** 2026-09-07T10:00:39Z
- **Completed:** 2026-09-07T10:06:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34109133973/job/101701026204)

#### Error Details

**Error 1:**
```
2026-09-07T10:02:06.6258018Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-09-07T10:02:06.6258706Z 
2026-09-07T10:02:09.0350520Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-09-07T10:02:09.0534971Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-09-07T10:02:09.0613590Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-09-07T10:04:05.5140274Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-09-07T10:04:07.9133461Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-07T10:04:07.9542688Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-07T10:04:07.9722267Z ../../
```

**Error 3:**
```
2026-09-07T10:04:07.9133461Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-07T10:04:07.9542688Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-07T10:04:07.9722267Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-07T10:04:07.9902394Z ../../../../reposi
```

**Error 4:**
```
2026-09-07T10:04:07.9542688Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-07T10:04:07.9722267Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-07T10:04:07.9902394Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-07T10:04:08.0090445Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-09-07T10:04:07.9722267Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-07T10:04:07.9902394Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-07T10:04:08.0090445Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-09-07T10:04:08.0281527Z ../../../../repositories/py
```

### 2. project_cpu_tests_linux (AllenCahn_Bayreuth)

- **Job ID:** 101701026584
- **Started:** 2026-09-07T10:00:39Z
- **Completed:** 2026-09-07T10:01:18Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34109133973/job/101701026584)

No specific error messages extracted. Check job logs for details.

### 3. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 101701026720
- **Started:** 2026-09-07T10:00:39Z
- **Completed:** 2026-09-07T10:03:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34109133973/job/101701026720)

#### Error Details

**Error 1:**
```
2026-09-07T10:01:52.1987012Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-07T10:01:52.2237579Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-07T10:01:52.2959226Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:01:52.3243845Z pySDC/test
```

**Error 2:**
```
2026-09-07T10:01:52.2237579Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-07T10:01:52.2959226Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:01:52.3243845Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:01:52.3529394Z pySDC/te
```

**Error 3:**
```
2026-09-07T10:01:52.2959226Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:01:52.3243845Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:01:52.3529394Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:01:52.3815480Z pySDC/
```

**Error 4:**
```
2026-09-07T10:01:52.3243845Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:01:52.3529394Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:01:52.3815480Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-07T10:01:52.4102623Z pySDC/
```

**Error 5:**
```
2026-09-07T10:01:52.3529394Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:01:52.3815480Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-07T10:01:52.4102623Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-07T10:01:52.4388984Z pySDC/tests/
```

### 4. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 101701026741
- **Started:** 2026-09-07T10:00:39Z
- **Completed:** 2026-09-07T10:16:23Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34109133973/job/101701026741)

#### Error Details

**Error 1:**
```
2026-09-07T10:16:21.2167441Z                     res = fixturedef.cached_result[0]
2026-09-07T10:16:21.2167944Z >                   pickle.dump(res, f)
2026-09-07T10:16:21.2168780Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-07T10:16:21.2169493Z 
2026-09-07T10:16:21.2170087Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 2:**
```
2026-09-07T10:16:21.2255866Z                     res = fixturedef.cached_result[0]
2026-09-07T10:16:21.2256357Z >                   pickle.dump(res, f)
2026-09-07T10:16:21.2257187Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-07T10:16:21.2257892Z 
2026-09-07T10:16:21.2258473Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 3:**
```
2026-09-07T10:16:21.2319957Z                     res = fixturedef.cached_result[0]
2026-09-07T10:16:21.2320244Z >                   pickle.dump(res, f)
2026-09-07T10:16:21.2320730Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-07T10:16:21.2321131Z 
2026-09-07T10:16:21.2321456Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 4:**
```
2026-09-07T10:16:21.2379418Z                     res = fixturedef.cached_result[0]
2026-09-07T10:16:21.2379704Z >                   pickle.dump(res, f)
2026-09-07T10:16:21.2380188Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-07T10:16:21.2380728Z 
2026-09-07T10:16:21.2381056Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

**Error 5:**
```
2026-09-07T10:16:21.2439011Z                     res = fixturedef.cached_result[0]
2026-09-07T10:16:21.2439296Z >                   pickle.dump(res, f)
2026-09-07T10:16:21.2439773Z E                   AttributeError: Can't pickle local object '_BaseExitStack._create_cb_wrapper.<locals>._exit_wrapper'
2026-09-07T10:16:21.2440174Z 
2026-09-07T10:16:21.2440503Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/pytest_isolate_mpi/_fixturecache.py:34: AttributeError
```

### 5. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 101701026758
- **Started:** 2026-09-07T10:02:48Z
- **Completed:** 2026-09-07T10:05:14Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34109133973/job/101701026758)

#### Error Details

**Error 1:**
```
2026-09-07T10:04:03.0246846Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-07T10:04:03.0432859Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-07T10:04:03.1128428Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:04:03.1347595Z pySDC/test
```

**Error 2:**
```
2026-09-07T10:04:03.0432859Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-07T10:04:03.1128428Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:04:03.1347595Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:04:03.1560577Z pySDC/te
```

**Error 3:**
```
2026-09-07T10:04:03.1128428Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:04:03.1347595Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:04:03.1560577Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:04:03.1773487Z pySDC/
```

**Error 4:**
```
2026-09-07T10:04:03.1347595Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:04:03.1560577Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:04:03.1773487Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-07T10:04:03.1992517Z pySDC/
```

**Error 5:**
```
2026-09-07T10:04:03.1560577Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:04:03.1773487Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-07T10:04:03.1992517Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-07T10:04:03.2207916Z pySDC/tests/
```

### 6. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 101701026864
- **Started:** 2026-09-07T10:03:18Z
- **Completed:** 2026-09-07T10:06:17Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34109133973/job/101701026864)

#### Error Details

**Error 1:**
```
2026-09-07T10:04:33.9687344Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-07T10:04:33.9957596Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-07T10:04:34.0934404Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:04:34.1229596Z pySDC/test
```

**Error 2:**
```
2026-09-07T10:04:33.9957596Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-07T10:04:34.0934404Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:04:34.1229596Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:04:34.1522144Z pySDC/te
```

**Error 3:**
```
2026-09-07T10:04:34.0934404Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-07T10:04:34.1229596Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:04:34.1522144Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:04:34.1827730Z pySDC/
```

**Error 4:**
```
2026-09-07T10:04:34.1229596Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-07T10:04:34.1522144Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:04:34.1827730Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-07T10:04:34.2128172Z pySDC/
```

**Error 5:**
```
2026-09-07T10:04:34.1522144Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-07T10:04:34.1827730Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-07T10:04:34.2128172Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-07T10:04:34.2421110Z pySDC/tests/
```

### 7. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 101701026893
- **Started:** 2026-09-07T10:03:01Z
- **Completed:** 2026-09-07T10:03:47Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/34109133973/job/101701026893)

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
