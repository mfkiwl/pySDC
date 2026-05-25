# Automated Test Failure Analysis

**Generated:** 2026-05-25T09:16:32.152047+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/26392431748

## Summary

- Total Jobs: 30
- Failed Jobs: 4

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 77685073976
- **Started:** 2026-05-25T08:59:03Z
- **Completed:** 2026-05-25T09:06:05Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26392431748/job/77685073976)

#### Error Details

**Error 1:**
```
2026-05-25T09:00:27.3691657Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-05-25T09:00:27.3692018Z 
2026-05-25T09:00:30.7305494Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-05-25T09:00:30.7553224Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-05-25T09:00:30.7652324Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-05-25T09:03:02.4694387Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-05-25T09:03:06.6498458Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-25T09:03:06.7137454Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-25T09:03:06.7387681Z ../../
```

**Error 3:**
```
2026-05-25T09:03:06.6498458Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-25T09:03:06.7137454Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-25T09:03:06.7387681Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-25T09:03:06.7641206Z ../../../../reposi
```

**Error 4:**
```
2026-05-25T09:03:06.7137454Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-25T09:03:06.7387681Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-25T09:03:06.7641206Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-25T09:03:06.7894289Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-05-25T09:03:06.7387681Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-25T09:03:06.7641206Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-25T09:03:06.7894289Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-05-25T09:03:06.8144738Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 77685074230
- **Started:** 2026-05-25T09:00:12Z
- **Completed:** 2026-05-25T09:03:03Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26392431748/job/77685074230)

#### Error Details

**Error 1:**
```
2026-05-25T09:01:22.6498176Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-25T09:01:22.6764292Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-25T09:01:22.7699160Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:01:22.7988780Z pySDC/test
```

**Error 2:**
```
2026-05-25T09:01:22.6764292Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-25T09:01:22.7699160Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:01:22.7988780Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:01:22.8273080Z pySDC/te
```

**Error 3:**
```
2026-05-25T09:01:22.7699160Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:01:22.7988780Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:01:22.8273080Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:01:22.8565268Z pySDC/
```

**Error 4:**
```
2026-05-25T09:01:22.7988780Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:01:22.8273080Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:01:22.8565268Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-25T09:01:22.8848106Z pySDC/
```

**Error 5:**
```
2026-05-25T09:01:22.8273080Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:01:22.8565268Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-25T09:01:22.8848106Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-25T09:01:22.9137236Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 77685074243
- **Started:** 2026-05-25T09:01:46Z
- **Completed:** 2026-05-25T09:04:39Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26392431748/job/77685074243)

#### Error Details

**Error 1:**
```
2026-05-25T09:02:57.8586666Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-25T09:02:57.8845824Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-25T09:02:57.9572855Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:02:57.9864992Z pySDC/test
```

**Error 2:**
```
2026-05-25T09:02:57.8845824Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-25T09:02:57.9572855Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:02:57.9864992Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:02:58.0163290Z pySDC/te
```

**Error 3:**
```
2026-05-25T09:02:57.9572855Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:02:57.9864992Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:02:58.0163290Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:02:58.0456574Z pySDC/
```

**Error 4:**
```
2026-05-25T09:02:57.9864992Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:02:58.0163290Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:02:58.0456574Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-25T09:02:58.0759827Z pySDC/
```

**Error 5:**
```
2026-05-25T09:02:58.0163290Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:02:58.0456574Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-25T09:02:58.0759827Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-25T09:02:58.1071280Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 77685074247
- **Started:** 2026-05-25T09:04:44Z
- **Completed:** 2026-05-25T09:07:56Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26392431748/job/77685074247)

#### Error Details

**Error 1:**
```
2026-05-25T09:06:01.8915022Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-25T09:06:01.9168499Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-25T09:06:02.0029611Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:06:02.0322137Z pySDC/test
```

**Error 2:**
```
2026-05-25T09:06:01.9168499Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-25T09:06:02.0029611Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:06:02.0322137Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:06:02.0609026Z pySDC/te
```

**Error 3:**
```
2026-05-25T09:06:02.0029611Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-25T09:06:02.0322137Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:06:02.0609026Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:06:02.0896203Z pySDC/
```

**Error 4:**
```
2026-05-25T09:06:02.0322137Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-25T09:06:02.0609026Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:06:02.0896203Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-25T09:06:02.1186377Z pySDC/
```

**Error 5:**
```
2026-05-25T09:06:02.0609026Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-25T09:06:02.0896203Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-25T09:06:02.1186377Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-25T09:06:02.1475192Z pySDC/tests/
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
