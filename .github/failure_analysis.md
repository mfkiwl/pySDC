# Automated Test Failure Analysis

**Generated:** 2026-04-27T07:51:41.173501+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/24982412587

## Summary

- Total Jobs: 30
- Failed Jobs: 4

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 73147508795
- **Started:** 2026-04-27T07:35:30Z
- **Completed:** 2026-04-27T07:42:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24982412587/job/73147508795)

#### Error Details

**Error 1:**
```
2026-04-27T07:36:48.0027768Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-04-27T07:36:48.0028235Z 
2026-04-27T07:36:50.9822033Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-04-27T07:36:51.0052064Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-04-27T07:36:51.0144712Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-04-27T07:39:23.6876006Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-04-27T07:39:25.7218894Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-04-27T07:39:25.7766292Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-04-27T07:39:25.8026029Z ../../
```

**Error 3:**
```
2026-04-27T07:39:25.7218894Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-04-27T07:39:25.7766292Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-04-27T07:39:25.8026029Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-04-27T07:39:25.8284108Z ../../../../reposi
```

**Error 4:**
```
2026-04-27T07:39:25.7766292Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-04-27T07:39:25.8026029Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-04-27T07:39:25.8284108Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-04-27T07:39:25.8554619Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-04-27T07:39:25.8026029Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-04-27T07:39:25.8284108Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-04-27T07:39:25.8554619Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-04-27T07:39:25.8816762Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 73147509042
- **Started:** 2026-04-27T07:35:31Z
- **Completed:** 2026-04-27T07:38:33Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24982412587/job/73147509042)

#### Error Details

**Error 1:**
```
2026-04-27T07:36:50.2393240Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-27T07:36:50.2646550Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-27T07:36:50.3403870Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:36:50.3703836Z pySDC/test
```

**Error 2:**
```
2026-04-27T07:36:50.2646550Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-27T07:36:50.3403870Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:36:50.3703836Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:36:50.4005445Z pySDC/te
```

**Error 3:**
```
2026-04-27T07:36:50.3403870Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:36:50.3703836Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:36:50.4005445Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:36:50.4306208Z pySDC/
```

**Error 4:**
```
2026-04-27T07:36:50.3703836Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:36:50.4005445Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:36:50.4306208Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-27T07:36:50.4611501Z pySDC/
```

**Error 5:**
```
2026-04-27T07:36:50.4005445Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:36:50.4306208Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-27T07:36:50.4611501Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-27T07:36:50.4911735Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 73147509061
- **Started:** 2026-04-27T07:37:36Z
- **Completed:** 2026-04-27T07:40:37Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24982412587/job/73147509061)

#### Error Details

**Error 1:**
```
2026-04-27T07:38:52.9482708Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-27T07:38:52.9751375Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-27T07:38:53.0505819Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:38:53.0823172Z pySDC/test
```

**Error 2:**
```
2026-04-27T07:38:52.9751375Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-27T07:38:53.0505819Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:38:53.0823172Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:38:53.1139458Z pySDC/te
```

**Error 3:**
```
2026-04-27T07:38:53.0505819Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:38:53.0823172Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:38:53.1139458Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:38:53.1453922Z pySDC/
```

**Error 4:**
```
2026-04-27T07:38:53.0823172Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:38:53.1139458Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:38:53.1453922Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-27T07:38:53.1764475Z pySDC/
```

**Error 5:**
```
2026-04-27T07:38:53.1139458Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:38:53.1453922Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-27T07:38:53.1764475Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-27T07:38:53.2084997Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 73147509065
- **Started:** 2026-04-27T07:39:12Z
- **Completed:** 2026-04-27T07:42:14Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24982412587/job/73147509065)

#### Error Details

**Error 1:**
```
2026-04-27T07:40:28.2768870Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-27T07:40:28.3044650Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-27T07:40:28.4032456Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:40:28.4332891Z pySDC/test
```

**Error 2:**
```
2026-04-27T07:40:28.3044650Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-27T07:40:28.4032456Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:40:28.4332891Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:40:28.4628605Z pySDC/te
```

**Error 3:**
```
2026-04-27T07:40:28.4032456Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-27T07:40:28.4332891Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:40:28.4628605Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:40:28.4924998Z pySDC/
```

**Error 4:**
```
2026-04-27T07:40:28.4332891Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-27T07:40:28.4628605Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:40:28.4924998Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-27T07:40:28.5211387Z pySDC/
```

**Error 5:**
```
2026-04-27T07:40:28.4628605Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-27T07:40:28.4924998Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-27T07:40:28.5211387Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-27T07:40:28.5505808Z pySDC/tests/
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
