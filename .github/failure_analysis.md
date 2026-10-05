# Automated Test Failure Analysis

**Generated:** 2026-10-05T12:25:58.141385+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/37307370036

## Summary

- Total Jobs: 30
- Failed Jobs: 10

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 111754193218
- **Started:** 2026-10-05T12:07:34Z
- **Completed:** 2026-10-05T12:08:57Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193218)

#### Error Details

**Error 1:**
```
2026-10-05T12:08:53.8480503Z Traceback (most recent call last):
2026-10-05T12:08:53.8480908Z   File "<string>", line 1, in <module>
```

**Error 2:**
```
2026-10-05T12:08:53.8484910Z   File "/repositories/gusto_repo/gusto/physics/chemistry.py", line 4, in <module>
2026-10-05T12:08:53.8485545Z     from firedrake.__future__ import interpolate
2026-10-05T12:08:53.8486508Z ImportError: cannot import name 'interpolate' from 'firedrake.__future__' (/opt/firedrake/firedrake/__future__.py). Did you mean: 'Interpolate'?
2026-10-05T12:08:54.4173429Z ##[error]Process completed with exit code 1.
2026-10-05T12:08:54.4295087Z Post job cleanup.
```

### 2. project_cpu_tests_linux (AllenCahn_Bayreuth)

- **Job ID:** 111754193399
- **Started:** 2026-10-05T12:07:34Z
- **Completed:** 2026-10-05T12:08:15Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193399)

No specific error messages extracted. Check job logs for details.

### 3. project_cpu_tests_linux (SDC_showdown)

- **Job ID:** 111754193420
- **Started:** 2026-10-05T12:07:34Z
- **Completed:** 2026-10-05T12:12:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193420)

No specific error messages extracted. Check job logs for details.

### 4. project_cpu_tests_linux (parallelSDC)

- **Job ID:** 111754193460
- **Started:** 2026-10-05T12:07:34Z
- **Completed:** 2026-10-05T12:08:22Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193460)

No specific error messages extracted. Check job logs for details.

### 5. user_cpu_tests_linux (mpi4py, 3.13)

- **Job ID:** 111754193505
- **Started:** 2026-10-05T12:08:34Z
- **Completed:** 2026-10-05T12:24:41Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193505)

#### Error Details

**Error 1:**
```
2026-10-05T12:24:37.5892924Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-05T12:24:37.5893315Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-05T12:24:37.5893826Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:24:37.5894081Z 
2026-10-05T12:24:37.5894461Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-10-05T12:24:37.5893826Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:24:37.5894081Z 
2026-10-05T12:24:37.5894461Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
2026-10-05T12:24:37.5895009Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-10-05T12:24:37.5895295Z 
```

**Error 3:**
```
2026-10-05T12:24:37.5917251Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-05T12:24:37.5917650Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-05T12:24:37.5917984Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:24:37.5918242Z 
2026-10-05T12:24:37.5918511Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-10-05T12:24:37.5917984Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:24:37.5918242Z 
2026-10-05T12:24:37.5918511Z ../../../micromamba/envs/pySDC/lib/python3.13/site-packages/_pytest/runner.py:527: AssertionError
2026-10-05T12:24:37.5919018Z =============================== warnings summary ===============================
2026-10-05T12:24:37.5919395Z pySDC/tests/test_helpers/test_fieldsIO.py: 2112 warnings
```

**Error 5:**
```
2026-10-05T12:24:37.6677862Z (1844 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-10-05T12:24:37.6678278Z =========================== short test summary info ============================
2026-10-05T12:24:37.6679049Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-10-05T12:24:37.6680102Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 6. user_cpu_tests_linux (mpi4py, 3.12)

- **Job ID:** 111754193549
- **Started:** 2026-10-05T12:07:33Z
- **Completed:** 2026-10-05T12:25:16Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193549)

#### Error Details

**Error 1:**
```
2026-10-05T12:25:14.2097139Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-05T12:25:14.2097539Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-05T12:25:14.2097868Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:25:14.2098431Z 
2026-10-05T12:25:14.2098848Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-10-05T12:25:14.2097868Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:25:14.2098431Z 
2026-10-05T12:25:14.2098848Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-10-05T12:25:14.2099409Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-10-05T12:25:14.2099704Z 
```

**Error 3:**
```
2026-10-05T12:25:14.2128311Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-05T12:25:14.2128730Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-05T12:25:14.2129078Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:25:14.2129421Z 
2026-10-05T12:25:14.2129911Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-10-05T12:25:14.2129078Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:25:14.2129421Z 
2026-10-05T12:25:14.2129911Z ../../../micromamba/envs/pySDC/lib/python3.12/site-packages/_pytest/runner.py:527: AssertionError
2026-10-05T12:25:14.2130496Z =============================== warnings summary ===============================
2026-10-05T12:25:14.2130885Z pySDC/tests/test_helpers/test_fieldsIO.py: 2112 warnings
```

**Error 5:**
```
2026-10-05T12:25:14.2950134Z (1833 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-10-05T12:25:14.2950668Z =========================== short test summary info ============================
2026-10-05T12:25:14.2951669Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-10-05T12:25:14.2953097Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 7. project_cpu_tests_linux (Resilience)

- **Job ID:** 111754193561
- **Started:** 2026-10-05T12:10:10Z
- **Completed:** 2026-10-05T12:11:11Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193561)

No specific error messages extracted. Check job logs for details.

### 8. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 111754193583
- **Started:** 2026-10-05T12:07:34Z
- **Completed:** 2026-10-05T12:10:35Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193583)

#### Error Details

**Error 1:**
```
2026-10-05T12:08:51.4518829Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-10-05T12:08:51.4794695Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-05T12:08:51.5604314Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-05T12:08:51.5967805Z pySDC/test
```

**Error 2:**
```
2026-10-05T12:08:51.4794695Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-05T12:08:51.5604314Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-05T12:08:51.5967805Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-05T12:08:51.6289543Z pySDC/te
```

**Error 3:**
```
2026-10-05T12:08:51.5604314Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-05T12:08:51.5967805Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-05T12:08:51.6289543Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-05T12:08:51.6602806Z pySDC/
```

**Error 4:**
```
2026-10-05T12:08:51.5967805Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-05T12:08:51.6289543Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-05T12:08:51.6602806Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-05T12:08:51.6919593Z pySDC/
```

**Error 5:**
```
2026-10-05T12:08:51.6289543Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-05T12:08:51.6602806Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-05T12:08:51.6919593Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-10-05T12:08:51.7243896Z pySDC/tests/
```

### 9. user_cpu_tests_linux (mpi4py, 3.11)

- **Job ID:** 111754193590
- **Started:** 2026-10-05T12:07:34Z
- **Completed:** 2026-10-05T12:22:05Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193590)

#### Error Details

**Error 1:**
```
2026-10-05T12:22:01.9176544Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-05T12:22:01.9177005Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-05T12:22:01.9177408Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:22:01.9177730Z 
2026-10-05T12:22:01.9178199Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 2:**
```
2026-10-05T12:22:01.9177408Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:22:01.9177730Z 
2026-10-05T12:22:01.9178199Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
2026-10-05T12:22:01.9178879Z _____________ ERROR at setup of test_MPI_nonMPI_consistency[2-32] ______________
2026-10-05T12:22:01.9179238Z 
```

**Error 3:**
```
2026-10-05T12:22:01.9204286Z >           assert col in needed_collectors, "previous item was not torn down properly"
2026-10-05T12:22:01.9204790Z                    ^^^^^^^^^^^^^^^^^^^^^^^^
2026-10-05T12:22:01.9205223Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:22:01.9205557Z 
2026-10-05T12:22:01.9205904Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
```

**Error 4:**
```
2026-10-05T12:22:01.9205223Z E           AssertionError: previous item was not torn down properly
2026-10-05T12:22:01.9205557Z 
2026-10-05T12:22:01.9205904Z ../../../micromamba/envs/pySDC/lib/python3.11/site-packages/_pytest/runner.py:527: AssertionError
2026-10-05T12:22:01.9206557Z =============================== warnings summary ===============================
2026-10-05T12:22:01.9207222Z pySDC/tests/test_problems/test_GrayScottMPIFFT.py::test_GrayScottMPIFFT[True-mi_diffusion]
```

**Error 5:**
```
2026-10-05T12:22:02.0387376Z (1852 durations < 0.005s hidden.  Use -vv to show these durations.)
2026-10-05T12:22:02.0387690Z =========================== short test summary info ============================
2026-10-05T12:22:02.0388275Z ERROR pySDC/tests/test_helpers/test_spectral_helper_1d_fft.py::test_differentiation_matrix[None--4-9] - AssertionError: previous item was not torn down properly
2026-10-05T12:22:02.0389144Z ERROR pySDC/tests/test_transfer_classes/test_base_transfer_MPI.py::test_MP
```

### 10. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 111754193610
- **Started:** 2026-10-05T12:08:37Z
- **Completed:** 2026-10-05T12:11:41Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/37307370036/job/111754193610)

#### Error Details

**Error 1:**
```
2026-10-05T12:10:00.5079665Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-10-05T12:10:00.5336219Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-05T12:10:00.6213173Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-05T12:10:00.6495020Z pySDC/test
```

**Error 2:**
```
2026-10-05T12:10:00.5336219Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-10-05T12:10:00.6213173Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-05T12:10:00.6495020Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-05T12:10:00.6777044Z pySDC/te
```

**Error 3:**
```
2026-10-05T12:10:00.6213173Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-10-05T12:10:00.6495020Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-05T12:10:00.6777044Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-05T12:10:00.7061510Z pySDC/
```

**Error 4:**
```
2026-10-05T12:10:00.6495020Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-10-05T12:10:00.6777044Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-05T12:10:00.7061510Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-05T12:10:00.7360079Z pySDC/
```

**Error 5:**
```
2026-10-05T12:10:00.6777044Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-10-05T12:10:00.7061510Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-10-05T12:10:00.7360079Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-10-05T12:10:00.7674308Z pySDC/tests/
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
