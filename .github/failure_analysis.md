# Automated Test Failure Analysis

**Generated:** 2026-03-16T06:36:10.064169+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/23130700563

## Summary

- Total Jobs: 30
- Failed Jobs: 1

## Failed Jobs

### 1. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 67183238218
- **Started:** 2026-03-16T06:20:51Z
- **Completed:** 2026-03-16T06:24:04Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/23130700563/job/67183238218)

#### Error Details

**Error 1:**
```
2026-03-16T06:22:10.5923921Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-03-16T06:22:10.6172850Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-03-16T06:22:10.7067504Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-03-16T06:22:10.7350381Z pySDC/test
```

**Error 2:**
```
2026-03-16T06:22:10.6172850Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-03-16T06:22:10.7067504Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-03-16T06:22:10.7350381Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-03-16T06:22:10.7633694Z pySDC/te
```

**Error 3:**
```
2026-03-16T06:22:10.7067504Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-03-16T06:22:10.7350381Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-03-16T06:22:10.7633694Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-03-16T06:22:10.7916887Z pySDC/
```

**Error 4:**
```
2026-03-16T06:22:10.7350381Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-03-16T06:22:10.7633694Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-03-16T06:22:10.7916887Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-03-16T06:22:10.8205657Z pySDC/
```

**Error 5:**
```
2026-03-16T06:22:10.7633694Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-03-16T06:22:10.7916887Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-03-16T06:22:10.8205657Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-03-16T06:22:10.8492271Z pySDC/tests/
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
