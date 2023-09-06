# RPATH

It is fairly straightforward to link to a library using RPATH.
This CMake file illustrates how to do that.


## What is it?

1. `context1.c`, `context1.h`, `context2.c`, `context2.h`, `global.c`, `global.h`:
   C source files that will be linked into a shared library.
1. `main.c`: application that uses the shared library.
1. `CMakeLists.txt`: CMake file to build the application using RPATH.
