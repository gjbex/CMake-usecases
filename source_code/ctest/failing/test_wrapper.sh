# test_wrapper.sh
#!/usr/bin/env bash
"$@"; rc=$?
echo "CTEST_EXIT_CODE=$rc" >&2   # goes into CTest's captured stderr
exit "$rc"
