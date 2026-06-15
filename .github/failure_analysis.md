# Automated Test Failure Analysis

**Generated:** 2026-06-15T11:11:59.208106+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/27541468059

## Summary

- Total Jobs: 30
- Failed Jobs: 4

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 81404060505
- **Started:** 2026-06-15T10:56:21Z
- **Completed:** 2026-06-15T11:03:39Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27541468059/job/81404060505)

#### Error Details

**Error 1:**
```
2026-06-15T10:57:47.7886479Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-06-15T10:57:47.7887007Z 
2026-06-15T10:57:51.1070520Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-06-15T10:57:51.1291084Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-06-15T10:57:51.1381786Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-06-15T11:00:27.9714955Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-06-15T11:00:30.2066273Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-15T11:00:30.2694603Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-15T11:00:30.2946124Z ../../
```

**Error 3:**
```
2026-06-15T11:00:30.2066273Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-15T11:00:30.2694603Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-15T11:00:30.2946124Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-15T11:00:30.3207366Z ../../../../reposi
```

**Error 4:**
```
2026-06-15T11:00:30.2694603Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-15T11:00:30.2946124Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-15T11:00:30.3207366Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-15T11:00:30.3488245Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-06-15T11:00:30.2946124Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-15T11:00:30.3207366Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-15T11:00:30.3488245Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-06-15T11:00:30.3768667Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 81404060838
- **Started:** 2026-06-15T10:57:45Z
- **Completed:** 2026-06-15T11:00:48Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27541468059/job/81404060838)

#### Error Details

**Error 1:**
```
2026-06-15T10:59:01.3449181Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-15T10:59:01.3727389Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-15T10:59:01.4730517Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:59:01.5051926Z pySDC/test
```

**Error 2:**
```
2026-06-15T10:59:01.3727389Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-15T10:59:01.4730517Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:59:01.5051926Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:59:01.5355095Z pySDC/te
```

**Error 3:**
```
2026-06-15T10:59:01.4730517Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:59:01.5051926Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:59:01.5355095Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:59:01.5669249Z pySDC/
```

**Error 4:**
```
2026-06-15T10:59:01.5051926Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:59:01.5355095Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:59:01.5669249Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-15T10:59:01.5972587Z pySDC/
```

**Error 5:**
```
2026-06-15T10:59:01.5355095Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:59:01.5669249Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-15T10:59:01.5972587Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-15T10:59:01.6281698Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 81404060840
- **Started:** 2026-06-15T10:58:30Z
- **Completed:** 2026-06-15T11:01:43Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27541468059/job/81404060840)

#### Error Details

**Error 1:**
```
2026-06-15T10:59:48.0809417Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-15T10:59:48.1063725Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-15T10:59:48.1950834Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:59:48.2243793Z pySDC/test
```

**Error 2:**
```
2026-06-15T10:59:48.1063725Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-15T10:59:48.1950834Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:59:48.2243793Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:59:48.2535038Z pySDC/te
```

**Error 3:**
```
2026-06-15T10:59:48.1950834Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:59:48.2243793Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:59:48.2535038Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:59:48.2834549Z pySDC/
```

**Error 4:**
```
2026-06-15T10:59:48.2243793Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:59:48.2535038Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:59:48.2834549Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-15T10:59:48.3140038Z pySDC/
```

**Error 5:**
```
2026-06-15T10:59:48.2535038Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:59:48.2834549Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-15T10:59:48.3140038Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-15T10:59:48.3433236Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 81404060863
- **Started:** 2026-06-15T10:57:26Z
- **Completed:** 2026-06-15T11:00:17Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27541468059/job/81404060863)

#### Error Details

**Error 1:**
```
2026-06-15T10:58:38.0008406Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-15T10:58:38.0267008Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-15T10:58:38.0999207Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:58:38.1296658Z pySDC/test
```

**Error 2:**
```
2026-06-15T10:58:38.0267008Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-15T10:58:38.0999207Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:58:38.1296658Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:58:38.1593952Z pySDC/te
```

**Error 3:**
```
2026-06-15T10:58:38.0999207Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-15T10:58:38.1296658Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:58:38.1593952Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:58:38.1892992Z pySDC/
```

**Error 4:**
```
2026-06-15T10:58:38.1296658Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-15T10:58:38.1593952Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:58:38.1892992Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-15T10:58:38.2187826Z pySDC/
```

**Error 5:**
```
2026-06-15T10:58:38.1593952Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-15T10:58:38.1892992Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-15T10:58:38.2187826Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-15T10:58:38.2492396Z pySDC/tests/
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
