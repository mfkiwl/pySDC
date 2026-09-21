# Automated Test Failure Analysis

**Generated:** 2026-09-21T10:49:19.508041+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/35589079745

## Summary

- Total Jobs: 30
- Failed Jobs: 6

## Failed Jobs

### 1. project_cpu_tests_linux (parallelSDC_reloaded)

- **Job ID:** 106299121408
- **Started:** 2026-09-21T10:31:15Z
- **Completed:** 2026-09-21T10:32:01Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/35589079745/job/106299121408)

No specific error messages extracted. Check job logs for details.

### 2. project_cpu_tests_linux (SDC_showdown)

- **Job ID:** 106299121417
- **Started:** 2026-09-21T10:30:15Z
- **Completed:** 2026-09-21T10:34:47Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/35589079745/job/106299121417)

No specific error messages extracted. Check job logs for details.

### 3. user_firedrake_tests

- **Job ID:** 106299121440
- **Started:** 2026-09-21T10:31:55Z
- **Completed:** 2026-09-21T10:39:18Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/35589079745/job/106299121440)

#### Error Details

**Error 1:**
```
2026-09-21T10:33:18.5657998Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-09-21T10:33:18.5658552Z 
2026-09-21T10:33:22.0784876Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-09-21T10:33:22.1019870Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-09-21T10:33:22.1134166Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-09-21T10:36:05.8006328Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-09-21T10:36:10.0951473Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-21T10:36:10.1614148Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-21T10:36:10.1880786Z ../../
```

**Error 3:**
```
2026-09-21T10:36:10.0951473Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-21T10:36:10.1614148Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-21T10:36:10.1880786Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-21T10:36:10.2146085Z ../../../../reposi
```

**Error 4:**
```
2026-09-21T10:36:10.1614148Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-21T10:36:10.1880786Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-21T10:36:10.2146085Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-21T10:36:10.2420788Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-09-21T10:36:10.1880786Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-21T10:36:10.2146085Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-21T10:36:10.2420788Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-09-21T10:36:10.2701601Z ../../../../repositories/py
```

### 4. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 106299121470
- **Started:** 2026-09-21T10:30:14Z
- **Completed:** 2026-09-21T10:33:10Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/35589079745/job/106299121470)

#### Error Details

**Error 1:**
```
2026-09-21T10:31:30.2316010Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-21T10:31:30.2602550Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-21T10:31:30.3368731Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-21T10:31:30.3685581Z pySDC/test
```

**Error 2:**
```
2026-09-21T10:31:30.2602550Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-21T10:31:30.3368731Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-21T10:31:30.3685581Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-21T10:31:30.4002477Z pySDC/te
```

**Error 3:**
```
2026-09-21T10:31:30.3368731Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-21T10:31:30.3685581Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-21T10:31:30.4002477Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-21T10:31:30.4323153Z pySDC/
```

**Error 4:**
```
2026-09-21T10:31:30.3685581Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-21T10:31:30.4002477Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-21T10:31:30.4323153Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-21T10:31:30.4644368Z pySDC/
```

**Error 5:**
```
2026-09-21T10:31:30.4002477Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-21T10:31:30.4323153Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-21T10:31:30.4644368Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-21T10:31:30.4958265Z pySDC/tests/
```

### 5. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 106299121507
- **Started:** 2026-09-21T10:30:15Z
- **Completed:** 2026-09-21T10:33:18Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/35589079745/job/106299121507)

#### Error Details

**Error 1:**
```
2026-09-21T10:31:37.1347756Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-21T10:31:37.1601918Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-21T10:31:37.2451432Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-21T10:31:37.2725873Z pySDC/test
```

**Error 2:**
```
2026-09-21T10:31:37.1601918Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-21T10:31:37.2451432Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-21T10:31:37.2725873Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-21T10:31:37.2996918Z pySDC/te
```

**Error 3:**
```
2026-09-21T10:31:37.2451432Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-21T10:31:37.2725873Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-21T10:31:37.2996918Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-21T10:31:37.3269042Z pySDC/
```

**Error 4:**
```
2026-09-21T10:31:37.2725873Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-21T10:31:37.2996918Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-21T10:31:37.3269042Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-21T10:31:37.3552202Z pySDC/
```

**Error 5:**
```
2026-09-21T10:31:37.2996918Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-21T10:31:37.3269042Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-21T10:31:37.3552202Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-21T10:31:37.3831531Z pySDC/tests/
```

### 6. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 106299121526
- **Started:** 2026-09-21T10:30:14Z
- **Completed:** 2026-09-21T10:47:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/35589079745/job/106299121526)

#### Error Details

**Error 1:**
```
2026-09-21T10:47:47.6693974Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-21T10:47:47.6694363Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-21T10:47:47.6694691Z E           AssertionError: previous item was not torn down properly
2026-09-21T10:47:47.6694945Z 
2026-09-21T10:47:47.6695341Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-09-21T10:47:47.6694691Z E           AssertionError: previous item was not torn down properly
2026-09-21T10:47:47.6694945Z 
2026-09-21T10:47:47.6695341Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-09-21T10:47:47.6695894Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-09-21T10:47:47.6696173Z 
```

**Error 3:**
```
2026-09-21T10:47:47.6724002Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-21T10:47:47.6724412Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-21T10:47:47.6724759Z E           AssertionError: previous item was not torn down properly
2026-09-21T10:47:47.6725029Z 
2026-09-21T10:47:47.6725303Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-09-21T10:47:47.6724759Z E           AssertionError: previous item was not torn down properly
2026-09-21T10:47:47.6725029Z 
2026-09-21T10:47:47.6725303Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-09-21T10:47:47.6725813Z =============================== warnings summary ===============================
2026-09-21T10:47:47.6726203Z pySDC/tests/test_helpers/test_fieldsIO.py: 2112 warnings
```

**Error 5:**
```
2026-09-21T10:47:47.8031104Z (1831 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-09-21T10:47:47.8031679Z =========================== short test summary info ============================
2026-09-21T10:47:47.8032760Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-09-21T10:47:47.8034257Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
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
