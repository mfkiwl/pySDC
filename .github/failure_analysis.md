# Automated Test Failure Analysis

**Generated:** 2026-04-06T07:13:10.379361+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/24022250039

## Summary

- Total Jobs: 30
- Failed Jobs: 5

## Failed Jobs

### 1. project_cpu_tests_linux (RayleighBenard)

- **Job ID:** 70053373565
- **Started:** 2026-04-06T06:56:45Z
- **Completed:** 2026-04-06T06:58:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24022250039/job/70053373565)

No specific error messages extracted. Check job logs for details.

### 2. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 70053373573
- **Started:** 2026-04-06T06:55:35Z
- **Completed:** 2026-04-06T06:58:20Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24022250039/job/70053373573)

#### Error Details

**Error 1:**
```
2026-04-06T06:56:49.1705237Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-06T06:56:49.1960792Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-06T06:56:49.2552763Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T06:56:49.2845449Z pySDC/test
```

**Error 2:**
```
2026-04-06T06:56:49.1960792Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-06T06:56:49.2552763Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T06:56:49.2845449Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T06:56:49.3139287Z pySDC/te
```

**Error 3:**
```
2026-04-06T06:56:49.2552763Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T06:56:49.2845449Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T06:56:49.3139287Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T06:56:49.3431426Z pySDC/
```

**Error 4:**
```
2026-04-06T06:56:49.2845449Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T06:56:49.3139287Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T06:56:49.3431426Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-06T06:56:49.3715405Z pySDC/
```

**Error 5:**
```
2026-04-06T06:56:49.3139287Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T06:56:49.3431426Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-06T06:56:49.3715405Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-06T06:56:49.4004555Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 70053373580
- **Started:** 2026-04-06T06:57:46Z
- **Completed:** 2026-04-06T07:00:37Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24022250039/job/70053373580)

#### Error Details

**Error 1:**
```
2026-04-06T06:58:57.5427763Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-06T06:58:57.5694322Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-06T06:58:57.6641580Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T06:58:57.6935099Z pySDC/test
```

**Error 2:**
```
2026-04-06T06:58:57.5694322Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-06T06:58:57.6641580Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T06:58:57.6935099Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T06:58:57.7229280Z pySDC/te
```

**Error 3:**
```
2026-04-06T06:58:57.6641580Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T06:58:57.6935099Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T06:58:57.7229280Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T06:58:57.7523675Z pySDC/
```

**Error 4:**
```
2026-04-06T06:58:57.6935099Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T06:58:57.7229280Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T06:58:57.7523675Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-06T06:58:57.7810531Z pySDC/
```

**Error 5:**
```
2026-04-06T06:58:57.7229280Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T06:58:57.7523675Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-06T06:58:57.7810531Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-06T06:58:57.8101496Z pySDC/tests/
```

### 4. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 70053373582
- **Started:** 2026-04-06T06:58:55Z
- **Completed:** 2026-04-06T07:02:07Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24022250039/job/70053373582)

#### Error Details

**Error 1:**
```
2026-04-06T07:00:11.9965306Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-06T07:00:12.0226315Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-06T07:00:12.1110067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T07:00:12.1405764Z pySDC/test
```

**Error 2:**
```
2026-04-06T07:00:12.0226315Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-06T07:00:12.1110067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T07:00:12.1405764Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T07:00:12.1699006Z pySDC/te
```

**Error 3:**
```
2026-04-06T07:00:12.1110067Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-06T07:00:12.1405764Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T07:00:12.1699006Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T07:00:12.1994730Z pySDC/
```

**Error 4:**
```
2026-04-06T07:00:12.1405764Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-06T07:00:12.1699006Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T07:00:12.1994730Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-06T07:00:12.2289081Z pySDC/
```

**Error 5:**
```
2026-04-06T07:00:12.1699006Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-06T07:00:12.1994730Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-06T07:00:12.2289081Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-06T07:00:12.2592050Z pySDC/tests/
```

### 5. user_cpu_tests_linux (fenics, 3.13)

- **Job ID:** 70053373586
- **Started:** 2026-04-06T06:59:34Z
- **Completed:** 2026-04-06T07:00:53Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24022250039/job/70053373586)

No specific error messages extracted. Check job logs for details.

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
