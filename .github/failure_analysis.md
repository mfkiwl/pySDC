# Automated Test Failure Analysis

**Generated:** 2026-06-08T09:42:17.640755+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/27128249512

## Summary

- Total Jobs: 30
- Failed Jobs: 3

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 80062340632
- **Started:** 2026-06-08T09:25:35Z
- **Completed:** 2026-06-08T09:32:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27128249512/job/80062340632)

#### Error Details

**Error 1:**
```
2026-06-08T09:27:01.7431832Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-06-08T09:27:01.7432412Z 
2026-06-08T09:27:05.1987692Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-06-08T09:27:05.2217151Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-06-08T09:27:05.2310890Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-06-08T09:29:43.9570267Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-06-08T09:29:46.1247136Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-08T09:29:46.1874881Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-08T09:29:46.2127971Z ../../
```

**Error 3:**
```
2026-06-08T09:29:46.1247136Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-08T09:29:46.1874881Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-08T09:29:46.2127971Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-08T09:29:46.2370466Z ../../../../reposi
```

**Error 4:**
```
2026-06-08T09:29:46.1874881Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-08T09:29:46.2127971Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-08T09:29:46.2370466Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-08T09:29:46.2627362Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-06-08T09:29:46.2127971Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-08T09:29:46.2370466Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-08T09:29:46.2627362Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-06-08T09:29:46.2898458Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 80062341196
- **Started:** 2026-06-08T09:26:32Z
- **Completed:** 2026-06-08T09:29:48Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27128249512/job/80062341196)

#### Error Details

**Error 1:**
```
2026-06-08T09:27:52.5265811Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-08T09:27:52.5525153Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-08T09:27:52.6419133Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-08T09:27:52.6717337Z pySDC/test
```

**Error 2:**
```
2026-06-08T09:27:52.5525153Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-08T09:27:52.6419133Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-08T09:27:52.6717337Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-08T09:27:52.7013077Z pySDC/te
```

**Error 3:**
```
2026-06-08T09:27:52.6419133Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-08T09:27:52.6717337Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-08T09:27:52.7013077Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-08T09:27:52.7313673Z pySDC/
```

**Error 4:**
```
2026-06-08T09:27:52.6717337Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-08T09:27:52.7013077Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-08T09:27:52.7313673Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-08T09:27:52.7626468Z pySDC/
```

**Error 5:**
```
2026-06-08T09:27:52.7013077Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-08T09:27:52.7313673Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-08T09:27:52.7626468Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-08T09:27:52.7934066Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 80062341198
- **Started:** 2026-06-08T09:27:03Z
- **Completed:** 2026-06-08T09:29:49Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/27128249512/job/80062341198)

#### Error Details

**Error 1:**
```
2026-06-08T09:28:15.2855141Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-08T09:28:15.3111704Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-08T09:28:15.4181131Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-08T09:28:15.4498909Z pySDC/test
```

**Error 2:**
```
2026-06-08T09:28:15.3111704Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-08T09:28:15.4181131Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-08T09:28:15.4498909Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-08T09:28:15.4807031Z pySDC/te
```

**Error 3:**
```
2026-06-08T09:28:15.4181131Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-08T09:28:15.4498909Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-08T09:28:15.4807031Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-08T09:28:15.5137170Z pySDC/
```

**Error 4:**
```
2026-06-08T09:28:15.4498909Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-08T09:28:15.4807031Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-08T09:28:15.5137170Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-08T09:28:15.5447350Z pySDC/
```

**Error 5:**
```
2026-06-08T09:28:15.4807031Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-08T09:28:15.5137170Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-08T09:28:15.5447350Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-08T09:28:15.5763414Z pySDC/tests/
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
