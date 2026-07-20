# Automated Test Failure Analysis

**Generated:** 2026-07-20T08:29:33.058464+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/29726863447

## Summary

- Total Jobs: 30
- Failed Jobs: 5

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 88301878446
- **Started:** 2026-07-20T08:08:39Z
- **Completed:** 2026-07-20T08:15:43Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29726863447/job/88301878446)

#### Error Details

**Error 1:**
```
2026-07-20T08:10:00.6980836Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-07-20T08:10:00.6981142Z 
2026-07-20T08:10:03.7518840Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-07-20T08:10:03.7758827Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-07-20T08:10:03.7856729Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-07-20T08:12:39.9932443Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-07-20T08:12:42.0645164Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-20T08:12:42.1192445Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-20T08:12:42.1454007Z ../../
```

**Error 3:**
```
2026-07-20T08:12:42.0645164Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-07-20T08:12:42.1192445Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-20T08:12:42.1454007Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-20T08:12:42.1703799Z ../../../../reposi
```

**Error 4:**
```
2026-07-20T08:12:42.1192445Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-07-20T08:12:42.1454007Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-20T08:12:42.1703799Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-20T08:12:42.1957857Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-07-20T08:12:42.1454007Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-07-20T08:12:42.1703799Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-07-20T08:12:42.1957857Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-07-20T08:12:42.2210148Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 88301878495
- **Started:** 2026-07-20T08:08:39Z
- **Completed:** 2026-07-20T08:11:37Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29726863447/job/88301878495)

#### Error Details

**Error 1:**
```
2026-07-20T08:09:54.4882904Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-20T08:09:54.5165839Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-20T08:09:54.5910802Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:09:54.6210394Z pySDC/test
```

**Error 2:**
```
2026-07-20T08:09:54.5165839Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-20T08:09:54.5910802Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:09:54.6210394Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:09:54.6510840Z pySDC/te
```

**Error 3:**
```
2026-07-20T08:09:54.5910802Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:09:54.6210394Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:09:54.6510840Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:09:54.6811654Z pySDC/
```

**Error 4:**
```
2026-07-20T08:09:54.6210394Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:09:54.6510840Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:09:54.6811654Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-20T08:09:54.7111927Z pySDC/
```

**Error 5:**
```
2026-07-20T08:09:54.6510840Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:09:54.6811654Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-20T08:09:54.7111927Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-20T08:09:54.7416157Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 88301878523
- **Started:** 2026-07-20T08:08:40Z
- **Completed:** 2026-07-20T08:11:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29726863447/job/88301878523)

#### Error Details

**Error 1:**
```
2026-07-20T08:09:58.2238408Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-20T08:09:58.2491455Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-20T08:09:58.3374575Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:09:58.3670605Z pySDC/test
```

**Error 2:**
```
2026-07-20T08:09:58.2491455Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-20T08:09:58.3374575Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:09:58.3670605Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:09:58.3962429Z pySDC/te
```

**Error 3:**
```
2026-07-20T08:09:58.3374575Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:09:58.3670605Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:09:58.3962429Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:09:58.4253259Z pySDC/
```

**Error 4:**
```
2026-07-20T08:09:58.3670605Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:09:58.3962429Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:09:58.4253259Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-20T08:09:58.4551177Z pySDC/
```

**Error 5:**
```
2026-07-20T08:09:58.3962429Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:09:58.4253259Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-20T08:09:58.4551177Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-20T08:09:58.4843197Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 88301878557
- **Started:** 2026-07-20T08:09:46Z
- **Completed:** 2026-07-20T08:12:51Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29726863447/job/88301878557)

#### Error Details

**Error 1:**
```
2026-07-20T08:11:18.6257725Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-07-20T08:11:18.6512174Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-20T08:11:18.7285889Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:11:18.7580308Z pySDC/test
```

**Error 2:**
```
2026-07-20T08:11:18.6512174Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-07-20T08:11:18.7285889Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:11:18.7580308Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:11:18.7863361Z pySDC/te
```

**Error 3:**
```
2026-07-20T08:11:18.7285889Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-07-20T08:11:18.7580308Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:11:18.7863361Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:11:18.8148570Z pySDC/
```

**Error 4:**
```
2026-07-20T08:11:18.7580308Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-07-20T08:11:18.7863361Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:11:18.8148570Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-20T08:11:18.8431419Z pySDC/
```

**Error 5:**
```
2026-07-20T08:11:18.7863361Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-07-20T08:11:18.8148570Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-07-20T08:11:18.8431419Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-07-20T08:11:18.8720461Z pySDC/tests/
```

### 5. user_cpu_tests_linux (fenics, 3.13)

- **Job ID:** 88301878561
- **Started:** 2026-07-20T08:09:30Z
- **Completed:** 2026-07-20T08:10:41Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/29726863447/job/88301878561)

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
