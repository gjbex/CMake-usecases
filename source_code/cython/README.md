# Cython

Example of building Cython extensions.

## What is it?
1. `hello_world.pyx`: code to be compiled using Cython.
1. `CMakeLists.txt`: CMake file to build the extension.
1. `cmake`: CMake extensions to deal with cython, copied from scikit-build.
1. `say_hello.py`: script to load the compiled module.  Note that the code
    is executed upon import since no guard is in place.
