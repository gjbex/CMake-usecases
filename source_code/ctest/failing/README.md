# Failures

This directory contains tests fail on purpose. This is intended to observe the
output and log of CTest to learn how to diagnose failures.


## What is it?

1. `compute.c`: a simple C application that expects two numbers as command line
   arguments and prints the square root of their division.
1. `segfault.c`: a simple C application that causes a segmentation fault.
1. `CMakeLists.txt`: a CMake file to build the applications and define tests.
1. `test_wrapper.sh`: a bash script to run the applications and capture their exit
   status.


## How to use it?

Build the applications:
```bash
$ cmake  -B build/  -S .
$ cmake  --build build/
```

Run the tests:
```bash
$ ctest --test-dir build/
```

The log file can be found in `build/Testing/Temporary/LastTest.log`.
