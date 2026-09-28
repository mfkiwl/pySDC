# Automated Test Failure Analysis

**Generated:** 2026-09-28T11:51:40.483625+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/36416243795

## Summary

- Total Jobs: 30
- Failed Jobs: 10

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 108907968166
- **Started:** 2026-09-28T11:32:30Z
- **Completed:** 2026-09-28T11:38:09Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968166)

#### Error Details

**Error 1:**
```
2026-09-28T11:34:03.2277030Z collecting ... collected 4194 items / 4157 deselected / 37 selected
2026-09-28T11:34:03.2277518Z 
2026-09-28T11:34:05.4883720Z ../../../../repositories/pySDC/pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_polynomial_error_firedrake FAILED [  2%]
2026-09-28T11:34:05.5064502Z ../../../../repositories/pySDC/pySDC/tests/test_datatypes/test_firedrake_mesh.py::test_addition PASSED [  5%]
2026-09-28T11:34:05.5132402Z ../../../../repositories/pySDC/p
```

**Error 2:**
```
2026-09-28T11:35:53.7683246Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-1] PASSED [ 70%]
2026-09-28T11:35:56.4122239Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-28T11:35:56.4536792Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-28T11:35:56.4718638Z ../../
```

**Error 3:**
```
2026-09-28T11:35:56.4122239Z ../../../../repositories/pySDC/pySDC/tests/test_helpers/test_gusto_coupling.py::test_pySDC_integrator_MSSDC[False-4] PASSED [ 72%]
2026-09-28T11:35:56.4536792Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-28T11:35:56.4718638Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-28T11:35:56.4897492Z ../../../../reposi
```

**Error 4:**
```
2026-09-28T11:35:56.4536792Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[0] FAILED [ 75%]
2026-09-28T11:35:56.4718638Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-28T11:35:56.4897492Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-28T11:35:56.5082497Z ../../../../repositories/pySDC/pySDC/tests
```

**Error 5:**
```
2026-09-28T11:35:56.4718638Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_solve_system[3.14] FAILED [ 78%]
2026-09-28T11:35:56.4897492Z ../../../../repositories/pySDC/pySDC/tests/test_problems/test_heat_firedrake.py::test_eval_f FAILED [ 81%]
2026-09-28T11:35:56.5082497Z ../../../../repositories/pySDC/pySDC/tests/test_transfer_classes/test_firedrake_transfer.py::test_Firedrake_transfer FAILED [ 83%]
2026-09-28T11:35:56.5268338Z ../../../../repositories/py
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 108907968348
- **Started:** 2026-09-28T11:32:30Z
- **Completed:** 2026-09-28T11:34:56Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968348)

#### Error Details

**Error 1:**
```
2026-09-28T11:33:41.6628779Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-28T11:33:41.6820813Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-28T11:33:41.7578646Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:41.7802359Z pySDC/test
```

**Error 2:**
```
2026-09-28T11:33:41.6820813Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-28T11:33:41.7578646Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:41.7802359Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:41.8031572Z pySDC/te
```

**Error 3:**
```
2026-09-28T11:33:41.7578646Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:41.7802359Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:41.8031572Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:41.8270957Z pySDC/
```

**Error 4:**
```
2026-09-28T11:33:41.7802359Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:41.8031572Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:41.8270957Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-28T11:33:41.8503898Z pySDC/
```

**Error 5:**
```
2026-09-28T11:33:41.8031572Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:41.8270957Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-28T11:33:41.8503898Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-28T11:33:41.8726036Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 108907968475
- **Started:** 2026-09-28T11:32:31Z
- **Completed:** 2026-09-28T11:35:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968475)

#### Error Details

**Error 1:**
```
2026-09-28T11:33:48.7659282Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-28T11:33:48.7914483Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-28T11:33:48.8649098Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:48.8945594Z pySDC/test
```

**Error 2:**
```
2026-09-28T11:33:48.7914483Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-28T11:33:48.8649098Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:48.8945594Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:48.9240016Z pySDC/te
```

**Error 3:**
```
2026-09-28T11:33:48.8649098Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:48.8945594Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:48.9240016Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:48.9534211Z pySDC/
```

**Error 4:**
```
2026-09-28T11:33:48.8945594Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:48.9240016Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:48.9534211Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-28T11:33:48.9826489Z pySDC/
```

**Error 5:**
```
2026-09-28T11:33:48.9240016Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:48.9534211Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-28T11:33:48.9826489Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-28T11:33:49.0118018Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 108907968500
- **Started:** 2026-09-28T11:32:31Z
- **Completed:** 2026-09-28T11:35:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968500)

#### Error Details

**Error 1:**
```
2026-09-28T11:33:47.6684789Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-09-28T11:33:47.6925162Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-28T11:33:47.7815654Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:47.8086697Z pySDC/test
```

**Error 2:**
```
2026-09-28T11:33:47.6925162Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-09-28T11:33:47.7815654Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:47.8086697Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:47.8356110Z pySDC/te
```

**Error 3:**
```
2026-09-28T11:33:47.7815654Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-09-28T11:33:47.8086697Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:47.8356110Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:47.8625374Z pySDC/
```

**Error 4:**
```
2026-09-28T11:33:47.8086697Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-09-28T11:33:47.8356110Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:47.8625374Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-28T11:33:47.8900812Z pySDC/
```

**Error 5:**
```
2026-09-28T11:33:47.8356110Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-09-28T11:33:47.8625374Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-09-28T11:33:47.8900812Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-09-28T11:33:47.9171961Z pySDC/tests/
```

### 5. user_cpu_tests_linux (pytorch, 3.11)

- **Job ID:** 108907968559
- **Started:** 2026-09-28T11:33:25Z
- **Completed:** 2026-09-28T11:34:28Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968559)

No specific error messages extracted. Check job logs for details.

### 6. user_cpu_tests_linux (mpi4py, 3.10)

- **Job ID:** 108907968570
- **Started:** 2026-09-28T11:32:31Z
- **Completed:** 2026-09-28T11:48:27Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968570)

#### Error Details

**Error 1:**
```
2026-09-28T11:48:23.6504176Z         for col, (finalizers, exc) in self.stack.items():
2026-09-28T11:48:23.6504600Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:48:23.6505065Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:23.6505499Z 
2026-09-28T11:48:23.6505934Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-09-28T11:48:23.6505065Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:23.6505499Z 
2026-09-28T11:48:23.6505934Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:48:23.6506824Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-09-28T11:48:23.6507110Z 
```

**Error 3:**
```
2026-09-28T11:48:23.6534577Z         for col, (finalizers, exc) in self.stack.items():
2026-09-28T11:48:23.6535155Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:48:23.6535783Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:23.6536043Z 
2026-09-28T11:48:23.6536323Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-09-28T11:48:23.6535783Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:23.6536043Z 
2026-09-28T11:48:23.6536323Z ../../../micromamba/envs/pySDC/lib/python3.10/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:48:23.6536826Z =============================== warnings summary ===============================
2026-09-28T11:48:23.6537335Z pySDC/tests/test_problems/test_GrayScottMPIFFT.py::test_GrayScottMPIFFT[True-mi_diffusion]
```

**Error 5:**
```
2026-09-28T11:48:23.7549580Z (1825 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-09-28T11:48:23.7550091Z =========================== short test summary info ============================
2026-09-28T11:48:23.7551055Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-09-28T11:48:23.7552420Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 7. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 108907968586
- **Started:** 2026-09-28T11:33:29Z
- **Completed:** 2026-09-28T11:50:56Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968586)

#### Error Details

**Error 1:**
```
2026-09-28T11:50:54.3974449Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:50:54.3975354Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-28T11:50:54.3975952Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:50:54.3976428Z 
2026-09-28T11:50:54.3977087Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-09-28T11:50:54.3975952Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:50:54.3976428Z 
2026-09-28T11:50:54.3977087Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:50:54.3978115Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-09-28T11:50:54.3978642Z 
```

**Error 3:**
```
2026-09-28T11:50:54.4025639Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:50:54.4026257Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-28T11:50:54.4026740Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:50:54.4027103Z 
2026-09-28T11:50:54.4027597Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-09-28T11:50:54.4026740Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:50:54.4027103Z 
2026-09-28T11:50:54.4027597Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:50:54.4028585Z =============================== warnings summary ===============================
2026-09-28T11:50:54.4029117Z pySDC/tests/test_helpers/test_fieldsIO.py: 2112 warnings
```

**Error 5:**
```
2026-09-28T11:50:54.5210369Z (1833 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-09-28T11:50:54.5211092Z =========================== short test summary info ============================
2026-09-28T11:50:54.5212422Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-09-28T11:50:54.5214286Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 8. user_cpu_tests_linux (fenics, 3.12)

- **Job ID:** 108907968655
- **Started:** 2026-09-28T11:32:30Z
- **Completed:** 2026-09-28T11:33:35Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968655)

No specific error messages extracted. Check job logs for details.

### 9. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 108907968664
- **Started:** 2026-09-28T11:34:26Z
- **Completed:** 2026-09-28T11:48:36Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968664)

#### Error Details

**Error 1:**
```
2026-09-28T11:48:32.5639030Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:48:32.5639529Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-28T11:48:32.5639950Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:32.5640293Z 
2026-09-28T11:48:32.5640797Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-09-28T11:48:32.5639950Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:32.5640293Z 
2026-09-28T11:48:32.5640797Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:48:32.5641513Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-09-28T11:48:32.5641881Z 
```

**Error 3:**
```
2026-09-28T11:48:32.5668132Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:48:32.5668650Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-28T11:48:32.5669094Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:32.5669444Z 
2026-09-28T11:48:32.5669813Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-09-28T11:48:32.5669094Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:48:32.5669444Z 
2026-09-28T11:48:32.5669813Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:48:32.5670485Z =============================== warnings summary ===============================
2026-09-28T11:48:32.5671151Z pySDC/tests/test_problems/test_GrayScottMPIFFT.py::test_GrayScottMPIFFT[True-mi_diffusion]
```

**Error 5:**
```
2026-09-28T11:48:32.6426623Z (1855 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-09-28T11:48:32.6426947Z =========================== short test summary info ============================
2026-09-28T11:48:32.6427541Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-09-28T11:48:32.6428330Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 10. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 108907968751
- **Started:** 2026-09-28T11:33:37Z
- **Completed:** 2026-09-28T11:49:53Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/36416243795/job/108907968751)

#### Error Details

**Error 1:**
```
2026-09-28T11:49:51.3963459Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:49:51.3963840Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-28T11:49:51.3964163Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:49:51.3964411Z 
2026-09-28T11:49:51.3964790Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-09-28T11:49:51.3964163Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:49:51.3964411Z 
2026-09-28T11:49:51.3964790Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:49:51.3965331Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-09-28T11:49:51.3965605Z 
```

**Error 3:**
```
2026-09-28T11:49:51.3991494Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-09-28T11:49:51.3992142Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-09-28T11:49:51.3992474Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:49:51.3992726Z 
2026-09-28T11:49:51.3992988Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-09-28T11:49:51.3992474Z E           AssertionError: previous item was not torn down properly
2026-09-28T11:49:51.3992726Z 
2026-09-28T11:49:51.3992988Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
2026-09-28T11:49:51.3993477Z =============================== warnings summary ===============================
2026-09-28T11:49:51.3993853Z pySDC/tests/test_helpers/test_fieldsIO.py: 2112 warnings
```

**Error 5:**
```
2026-09-28T11:49:51.4979306Z (1845 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-09-28T11:49:51.4979700Z =========================== short test summary info ============================
2026-09-28T11:49:51.4980445Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-09-28T11:49:51.4981473Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
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
