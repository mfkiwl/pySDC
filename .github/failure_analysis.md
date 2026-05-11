# Automated Test Failure Analysis

**Generated:** 2026-05-11T08:44:23.308717+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/25658952996

## Summary

- Total Jobs: 30
- Failed Jobs: 3

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 75314316140
- **Started:** 2026-05-11T08:27:04Z
- **Completed:** 2026-05-11T08:34:08Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/25658952996/job/75314316140)

#### Error Details

**Error 1:**
```
2026-05-11T08:28:29.0006958Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-05-11T08:28:29.0007411Z 
2026-05-11T08:28:32.3331774Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-05-11T08:28:32.3554078Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-05-11T08:28:32.3643086Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-05-11T08:31:06.9971258Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-05-11T08:31:09.1829543Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-11T08:31:09.2482202Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-11T08:31:09.2725447Z ../../
```

**Error 3:**
```
2026-05-11T08:31:09.1829543Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-05-11T08:31:09.2482202Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-11T08:31:09.2725447Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-11T08:31:09.2957431Z ../../../../reposi
```

**Error 4:**
```
2026-05-11T08:31:09.2482202Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-05-11T08:31:09.2725447Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-11T08:31:09.2957431Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-11T08:31:09.3202199Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-05-11T08:31:09.2725447Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-05-11T08:31:09.2957431Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-05-11T08:31:09.3202199Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-05-11T08:31:09.3449179Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 75314316270
- **Started:** 2026-05-11T08:29:00Z
- **Completed:** 2026-05-11T08:31:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/25658952996/job/75314316270)

#### Error Details

**Error 1:**
```
2026-05-11T08:30:12.3283141Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-11T08:30:12.3536729Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-11T08:30:12.4251131Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-11T08:30:12.4545575Z pySDC/test
```

**Error 2:**
```
2026-05-11T08:30:12.3536729Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-11T08:30:12.4251131Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-11T08:30:12.4545575Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-11T08:30:12.4839193Z pySDC/te
```

**Error 3:**
```
2026-05-11T08:30:12.4251131Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-11T08:30:12.4545575Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-11T08:30:12.4839193Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-11T08:30:12.5134200Z pySDC/
```

**Error 4:**
```
2026-05-11T08:30:12.4545575Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-11T08:30:12.4839193Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-11T08:30:12.5134200Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-11T08:30:12.5427536Z pySDC/
```

**Error 5:**
```
2026-05-11T08:30:12.4839193Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-11T08:30:12.5134200Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-11T08:30:12.5427536Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-11T08:30:12.5726974Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 75314316274
- **Started:** 2026-05-11T08:26:08Z
- **Completed:** 2026-05-11T08:28:50Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/25658952996/job/75314316274)

#### Error Details

**Error 1:**
```
2026-05-11T08:27:17.2762543Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-05-11T08:27:17.3036100Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-11T08:27:17.4029675Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-11T08:27:17.4359004Z pySDC/test
```

**Error 2:**
```
2026-05-11T08:27:17.3036100Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-05-11T08:27:17.4029675Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-11T08:27:17.4359004Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-11T08:27:17.4694526Z pySDC/te
```

**Error 3:**
```
2026-05-11T08:27:17.4029675Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-05-11T08:27:17.4359004Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-11T08:27:17.4694526Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-11T08:27:17.5019957Z pySDC/
```

**Error 4:**
```
2026-05-11T08:27:17.4359004Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-05-11T08:27:17.4694526Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-11T08:27:17.5019957Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-11T08:27:17.5335416Z pySDC/
```

**Error 5:**
```
2026-05-11T08:27:17.4694526Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-05-11T08:27:17.5019957Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-05-11T08:27:17.5335416Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-05-11T08:27:17.5655942Z pySDC/tests/
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
