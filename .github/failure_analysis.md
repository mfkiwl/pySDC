# Automated Test Failure Analysis

**Generated:** 2026-03-09T06:18:13.417425+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/22840511053

## Summary

- Total Jobs: 30
- Failed Jobs: 1

## Failed Jobs

### 1. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 66245586956
- **Started:** 2026-03-09T06:02:34Z
- **Completed:** 2026-03-09T06:05:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/22840511053/job/66245586956)

#### Error Details

**Error 1:**
```
2026-03-09T06:03:53.5516999Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-03-09T06:03:53.5770089Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-03-09T06:03:53.6571166Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-03-09T06:03:53.6866989Z pySDC/test
```

**Error 2:**
```
2026-03-09T06:03:53.5770089Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-03-09T06:03:53.6571166Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-03-09T06:03:53.6866989Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-03-09T06:03:53.7159324Z pySDC/te
```

**Error 3:**
```
2026-03-09T06:03:53.6571166Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-03-09T06:03:53.6866989Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-03-09T06:03:53.7159324Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-03-09T06:03:53.7456395Z pySDC/
```

**Error 4:**
```
2026-03-09T06:03:53.6866989Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-03-09T06:03:53.7159324Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-03-09T06:03:53.7456395Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-03-09T06:03:53.7751555Z pySDC/
```

**Error 5:**
```
2026-03-09T06:03:53.7159324Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-03-09T06:03:53.7456395Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-03-09T06:03:53.7751555Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-03-09T06:03:53.8054427Z pySDC/tests/
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
