# Automated Test Failure Analysis

**Generated:** 2026-04-20T07:31:38.535252+00:00
**Workflow Run:** https://github.com/mfkiwl/pySDC/actions/runs/24653607636

## Summary

- Total Jobs: 30
- Failed Jobs: 3

## Failed Jobs

### 1. user_firedrake_tests

- **Job ID:** 72081716522
- **Started:** 2026-04-20T07:18:14Z
- **Completed:** 2026-04-20T07:19:29Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24653607636/job/72081716522)

#### Error Details

**Error 1:**
```
2026-04-20T07:19:26.0000516Z Traceback (most recent call last):
2026-04-20T07:19:26.0000799Z   File "<string>", line 1, in <module>
```

**Error 2:**
```
2026-04-20T07:19:26.0007240Z   File "/repositories/gusto_repo/gusto/recovery/averaging.py", line 11, in <module>
2026-04-20T07:19:26.0007622Z     from firedrake.utils import cached_property
2026-04-20T07:19:26.0008093Z ImportError: cannot import name 'cached_property' from 'firedrake.utils' (/opt/firedrake/firedrake/utils.py)
2026-04-20T07:19:26.5614165Z WARNING! There are options you set that were not used!
2026-04-20T07:19:26.5614959Z WARNING! could be spelling mistake, etc!
```

### 2. user_cpu_tests_linux (base, 3.13)

- **Job ID:** 72081716721
- **Started:** 2026-04-20T07:20:28Z
- **Completed:** 2026-04-20T07:23:19Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24653607636/job/72081716721)

#### Error Details

**Error 1:**
```
2026-04-20T07:21:40.0202864Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-20T07:21:40.0468855Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-20T07:21:40.1198815Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-20T07:21:40.1496490Z pySDC/test
```

**Error 2:**
```
2026-04-20T07:21:40.0468855Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-20T07:21:40.1198815Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-20T07:21:40.1496490Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-20T07:21:40.1802204Z pySDC/te
```

**Error 3:**
```
2026-04-20T07:21:40.1198815Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-20T07:21:40.1496490Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-20T07:21:40.1802204Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-20T07:21:40.2098931Z pySDC/
```

**Error 4:**
```
2026-04-20T07:21:40.1496490Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-20T07:21:40.1802204Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-20T07:21:40.2098931Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-20T07:21:40.2397991Z pySDC/
```

**Error 5:**
```
2026-04-20T07:21:40.1802204Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-20T07:21:40.2098931Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-20T07:21:40.2397991Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-20T07:21:40.2720548Z pySDC/tests/
```

### 3. user_cpu_tests_linux (base, 3.12)

- **Job ID:** 72081716736
- **Started:** 2026-04-20T07:20:44Z
- **Completed:** 2026-04-20T07:23:52Z
- **Logs:** [View Job Logs](https://github.com/mfkiwl/pySDC/actions/runs/24653607636/job/72081716736)

#### Error Details

**Error 1:**
```
2026-04-20T07:21:58.8476476Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-3] PASSED [ 15%]
2026-04-20T07:21:58.8734131Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-20T07:21:58.9607533Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-20T07:21:58.9894790Z pySDC/test
```

**Error 2:**
```
2026-04-20T07:21:58.8734131Z pySDC/tests/test_convergence_controllers/test_extrapolation_within_Q.py::test_extrapolation_within_Q[GAUSS-4] PASSED [ 15%]
2026-04-20T07:21:58.9607533Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-20T07:21:58.9894790Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-20T07:21:59.0183949Z pySDC/te
```

**Error 3:**
```
2026-04-20T07:21:58.9607533Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-2] FAILED [ 15%]
2026-04-20T07:21:58.9894790Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-20T07:21:59.0183949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-20T07:21:59.0474346Z pySDC/
```

**Error 4:**
```
2026-04-20T07:21:58.9894790Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-3] FAILED [ 15%]
2026-04-20T07:21:59.0183949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-20T07:21:59.0474346Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-20T07:21:59.0768891Z pySDC/
```

**Error 5:**
```
2026-04-20T07:21:59.0183949Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-4] FAILED [ 15%]
2026-04-20T07:21:59.0474346Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-RADAU-RIGHT-5] FAILED [ 15%]
2026-04-20T07:21:59.0768891Z pySDC/tests/test_convergence_controllers/test_polynomial_error.py::test_interpolation_error[True-GAUSS-2] FAILED [ 15%]
2026-04-20T07:21:59.1060761Z pySDC/tests/
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
