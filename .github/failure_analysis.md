# Automated Test Failure Analysis

**Generated:** 2026-06-01T10:38:32.582174+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/26749164916

## Summary

- Total Jobs: 30
- Failed Jobs: 2

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 78832421744
- **Started:** 2026-06-01T10:23:23Z
- **Completed:** 2026-06-01T10:30:30Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26749164916/job/78832421744)

#### Error Details

**Error 1:**
```
2026-06-01T10:24:44.1772971Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-06-01T10:24:44.1773612Z 
2026-06-01T10:24:47.4865982Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-06-01T10:24:47.5089456Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-06-01T10:24:47.5182627Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-06-01T10:27:24.8165233Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-06-01T10:27:28.5655505Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-01T10:27:28.6257901Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-01T10:27:28.6488202Z ../../
```

**Error 3:**
```
2026-06-01T10:27:28.5655505Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-06-01T10:27:28.6257901Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-01T10:27:28.6488202Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-01T10:27:28.6708281Z ../../../../reposi
```

**Error 4:**
```
2026-06-01T10:27:28.6257901Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-06-01T10:27:28.6488202Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-01T10:27:28.6708281Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-01T10:27:28.6947301Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-06-01T10:27:28.6488202Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-06-01T10:27:28.6708281Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-06-01T10:27:28.6947301Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-06-01T10:27:28.7181621Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 78832421784
- **Started:** 2026-06-01T10:26:10Z
- **Completed:** 2026-06-01T10:28:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/26749164916/job/78832421784)

#### Error Details

**Error 1:**
```
2026-06-01T10:27:19.6374443Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-06-01T10:27:19.6628682Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-01T10:27:19.7644041Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-01T10:27:19.7959959Z pySDC/test
```

**Error 2:**
```
2026-06-01T10:27:19.6628682Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-06-01T10:27:19.7644041Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-01T10:27:19.7959959Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-01T10:27:19.8265768Z pySDC/te
```

**Error 3:**
```
2026-06-01T10:27:19.7644041Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-06-01T10:27:19.7959959Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-01T10:27:19.8265768Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-01T10:27:19.8573488Z pySDC/
```

**Error 4:**
```
2026-06-01T10:27:19.7959959Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-06-01T10:27:19.8265768Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-01T10:27:19.8573488Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-01T10:27:19.8879536Z pySDC/
```

**Error 5:**
```
2026-06-01T10:27:19.8265768Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-06-01T10:27:19.8573488Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-06-01T10:27:19.8879536Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-06-01T10:27:19.9199401Z pySDC/tests/
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
