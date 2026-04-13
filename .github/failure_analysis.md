# Automated Test Failure Analysis

**Generated:** 2026-04-13T07:32:39.462553+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/24330650448

## Summary

- Total Jobs: 30
- Failed Jobs: 3

## Failed Jobs

### 1. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 71035529538
- **Started:** 2026-04-13T07:15:35Z
- **Completed:** 2026-04-13T07:18:49Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24330650448/job/71035529538)

#### Error Details

**Error 1:**
```
2026-04-13T07:16:53.8655305Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-13T07:16:53.8913082Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-13T07:16:53.9783958Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:16:54.0084956Z pySDC/test
```

**Error 2:**
```
2026-04-13T07:16:53.8913082Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-13T07:16:53.9783958Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:16:54.0084956Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:16:54.0389102Z pySDC/te
```

**Error 3:**
```
2026-04-13T07:16:53.9783958Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:16:54.0084956Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:16:54.0389102Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:16:54.0701055Z pySDC/
```

**Error 4:**
```
2026-04-13T07:16:54.0084956Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:16:54.0389102Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:16:54.0701055Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-13T07:16:54.1019285Z pySDC/
```

**Error 5:**
```
2026-04-13T07:16:54.0389102Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:16:54.0701055Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-13T07:16:54.1019285Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-13T07:16:54.1326758Z pySDC/tests/
```

### 2. user_cpu_tests_linux (base, 3.11)

- **Job ID:** 71035529559
- **Started:** 2026-04-13T07:18:31Z
- **Completed:** 2026-04-13T07:21:31Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24330650448/job/71035529559)

#### Error Details

**Error 1:**
```
2026-04-13T07:19:45.8399349Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-13T07:19:45.8679185Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-13T07:19:45.9657365Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:19:45.9975101Z pySDC/test
```

**Error 2:**
```
2026-04-13T07:19:45.8679185Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-13T07:19:45.9657365Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:19:45.9975101Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:19:46.0282012Z pySDC/te
```

**Error 3:**
```
2026-04-13T07:19:45.9657365Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:19:45.9975101Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:19:46.0282012Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:19:46.0594174Z pySDC/
```

**Error 4:**
```
2026-04-13T07:19:45.9975101Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:19:46.0282012Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:19:46.0594174Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-13T07:19:46.0906195Z pySDC/
```

**Error 5:**
```
2026-04-13T07:19:46.0282012Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:19:46.0594174Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-13T07:19:46.0906195Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-13T07:19:46.1218795Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 71035529579
- **Started:** 2026-04-13T07:19:37Z
- **Completed:** 2026-04-13T07:22:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24330650448/job/71035529579)

#### Error Details

**Error 1:**
```
2026-04-13T07:20:49.5537414Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-13T07:20:49.5781439Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-13T07:20:49.6578127Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:20:49.6866557Z pySDC/test
```

**Error 2:**
```
2026-04-13T07:20:49.5781439Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-13T07:20:49.6578127Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:20:49.6866557Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:20:49.7149007Z pySDC/te
```

**Error 3:**
```
2026-04-13T07:20:49.6578127Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-13T07:20:49.6866557Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:20:49.7149007Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:20:49.7432578Z pySDC/
```

**Error 4:**
```
2026-04-13T07:20:49.6866557Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-13T07:20:49.7149007Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:20:49.7432578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-13T07:20:49.7716238Z pySDC/
```

**Error 5:**
```
2026-04-13T07:20:49.7149007Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-13T07:20:49.7432578Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-13T07:20:49.7716238Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-13T07:20:49.8008301Z pySDC/tests/
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
