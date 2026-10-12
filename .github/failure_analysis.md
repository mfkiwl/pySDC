# Automated Test Failure Analysis

**Generated:** 2026-10-12T13:11:54.143201+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/38251890721

## Summary

- Total Jobs: 30
- Failed Jobs: 8

## Failed Jobs

### 1. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 114820031200
- **Started:** 2026-10-12T12:53:23Z
- **Completed:** 2026-10-12T12:56:24Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031200)

#### Error Details

**Error 1:**
```
2026-10-12T12:54:40.9351273Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-10-12T12:54:40.9619945Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-12T12:54:41.0583812Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:54:41.0885073Z pySDC/test
```

**Error 2:**
```
2026-10-12T12:54:40.9619945Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-12T12:54:41.0583812Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:54:41.0885073Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:54:41.1185047Z pySDC/te
```

**Error 3:**
```
2026-10-12T12:54:41.0583812Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:54:41.0885073Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:54:41.1185047Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:54:41.1477443Z pySDC/
```

**Error 4:**
```
2026-10-12T12:54:41.0885073Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:54:41.1185047Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:54:41.1477443Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-12T12:54:41.1778277Z pySDC/
```

**Error 5:**
```
2026-10-12T12:54:41.1185047Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:54:41.1477443Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-12T12:54:41.1778277Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-10-12T12:54:41.2080158Z pySDC/tests/
```

### 2. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 114820031227
- **Started:** 2026-10-12T12:53:23Z
- **Completed:** 2026-10-12T13:11:07Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031227)

#### Error Details

**Error 1:**
```
2026-10-12T13:11:02.9385545Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-12T13:11:02.9385943Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-12T13:11:02.9386277Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:11:02.9386537Z 
2026-10-12T13:11:02.9386947Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-10-12T13:11:02.9386277Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:11:02.9386537Z 
2026-10-12T13:11:02.9386947Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-10-12T13:11:02.9387528Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-10-12T13:11:02.9387823Z 
```

**Error 3:**
```
2026-10-12T13:11:02.9418741Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-12T13:11:02.9419464Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-12T13:11:02.9420061Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:11:02.9420340Z 
2026-10-12T13:11:02.9420635Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-10-12T13:11:02.9420061Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:11:02.9420340Z 
2026-10-12T13:11:02.9420635Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-10-12T13:11:02.9421168Z =============================== warnings summary ===============================
2026-10-12T13:11:02.9421566Z pySDC/tests/test_helpers/test_fieldsIO.py: 2112 warnings
```

**Error 5:**
```
2026-10-12T13:11:03.0717342Z (1827 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-10-12T13:11:03.0717961Z =========================== short test summary info ============================
2026-10-12T13:11:03.0719253Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-10-12T13:11:03.0720877Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 3. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 114820031239
- **Started:** 2026-10-12T12:53:23Z
- **Completed:** 2026-10-12T12:54:11Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031239)

No specific error messages extracted. Check job logs for details.

### 4. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 114820031251
- **Started:** 2026-10-12T12:53:23Z
- **Completed:** 2026-10-12T12:55:44Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031251)

#### Error Details

**Error 1:**
```
2026-10-12T12:54:32.7849959Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-10-12T12:54:32.8052510Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-12T12:54:32.8635414Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:54:32.8853833Z pySDC/test
```

**Error 2:**
```
2026-10-12T12:54:32.8052510Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-12T12:54:32.8635414Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:54:32.8853833Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:54:32.9071049Z pySDC/te
```

**Error 3:**
```
2026-10-12T12:54:32.8635414Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:54:32.8853833Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:54:32.9071049Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:54:32.9288196Z pySDC/
```

**Error 4:**
```
2026-10-12T12:54:32.8853833Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:54:32.9071049Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:54:32.9288196Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-12T12:54:32.9504657Z pySDC/
```

**Error 5:**
```
2026-10-12T12:54:32.9071049Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:54:32.9288196Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-12T12:54:32.9504657Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-10-12T12:54:32.9726215Z pySDC/tests/
```

### 5. user_firedrake_tests

- **Job ID:** 114820031258
- **Started:** 2026-10-12T12:53:23Z
- **Completed:** 2026-10-12T12:57:50Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031258)

#### Error Details

**Error 1:**
```
2026-10-12T12:54:44.4564730Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-10-12T12:54:44.4565544Z 
2026-10-12T12:54:47.8994942Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-10-12T12:54:47.9226459Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-10-12T12:54:47.9320270Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-10-12T12:57:24.3127293Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-10-12T12:57:27.9841009Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-10-12T12:57:28.0472965Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-10-12T12:57:28.0729604Z ../../
```

**Error 3:**
```
2026-10-12T12:57:27.9841009Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-10-12T12:57:28.0472965Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-10-12T12:57:28.0729604Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-10-12T12:57:28.0979537Z ../../../../reposi
```

**Error 4:**
```
2026-10-12T12:57:28.0472965Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-10-12T12:57:28.0729604Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-10-12T12:57:28.0979537Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-10-12T12:57:28.1210849Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-10-12T12:57:28.0729604Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-10-12T12:57:28.0979537Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-10-12T12:57:28.1210849Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-10-12T12:57:28.1432178Z ../../../../repositories/py
```

### 6. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 114820031261
- **Started:** 2026-10-12T12:53:22Z
- **Completed:** 2026-10-12T13:09:55Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031261)

#### Error Details

**Error 1:**
```
2026-10-12T13:09:54.1119066Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-12T13:09:54.1119480Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-12T13:09:54.1119838Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:09:54.1120099Z 
2026-10-12T13:09:54.1120504Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-10-12T13:09:54.1119838Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:09:54.1120099Z 
2026-10-12T13:09:54.1120504Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
2026-10-12T13:09:54.1121085Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-10-12T13:09:54.1121771Z 
```

**Error 3:**
```
2026-10-12T13:09:54.1153599Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-12T13:09:54.1154283Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-12T13:09:54.1154668Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:09:54.1154957Z 
2026-10-12T13:09:54.1155258Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-10-12T13:09:54.1154668Z E           AssertionError: previous item was not torn down properly
2026-10-12T13:09:54.1154957Z 
2026-10-12T13:09:54.1155258Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
2026-10-12T13:09:54.1155797Z =============================== warnings summary ===============================
2026-10-12T13:09:54.1156481Z pySDC/tests/test_problems/test_GrayScottMPIFFT.py::test_GrayScottMPIFFT[True-mi_diffusion]
```

**Error 5:**
```
2026-10-12T13:09:54.1823222Z (1846 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-10-12T13:09:54.1823646Z =========================== short test summary info ============================
2026-10-12T13:09:54.1824412Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-10-12T13:09:54.1825465Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 7. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 114820031266
- **Started:** 2026-10-12T12:54:26Z
- **Completed:** 2026-10-12T12:55:11Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031266)

No specific error messages extracted. Check job logs for details.

### 8. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 114820031356
- **Started:** 2026-10-12T12:54:31Z
- **Completed:** 2026-10-12T12:57:36Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/38251890721/job/114820031356)

#### Error Details

**Error 1:**
```
2026-10-12T12:55:55.6522639Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-10-12T12:55:55.6769483Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-12T12:55:55.7641777Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:55:55.7918894Z pySDC/test
```

**Error 2:**
```
2026-10-12T12:55:55.6769483Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-12T12:55:55.7641777Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:55:55.7918894Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:55:55.8192370Z pySDC/te
```

**Error 3:**
```
2026-10-12T12:55:55.7641777Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-12T12:55:55.7918894Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:55:55.8192370Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:55:55.8466891Z pySDC/
```

**Error 4:**
```
2026-10-12T12:55:55.7918894Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-12T12:55:55.8192370Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:55:55.8466891Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-12T12:55:55.8745313Z pySDC/
```

**Error 5:**
```
2026-10-12T12:55:55.8192370Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-12T12:55:55.8466891Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-12T12:55:55.8745313Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-10-12T12:55:55.9016573Z pySDC/tests/
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
