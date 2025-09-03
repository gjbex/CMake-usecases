# CMake

CMake is a convenient build system, some example of using it are given in the
various subdirectories.

## What is this?

1. `simple`: trivial "hello world" example.
1. `library`: example of building and installing two applications that are
   linked to a library which is also built.
1. `external_library`: example of building and installing an application that is
   linked to a third-party library (GSL).
1. `sort`: example of a project that requires Catch2.
1. `ctest`: example of using CTest.
1. `doxygen`: example of generating doxygen documentation.
1. `clang_tidy`: example of invoking clang-tidy during the build process.
1. `blas_lapack/`: example of using BLAS and Lapack, as well as specifying
   a specific BLAS/LAPACK implementation (i.e., MKL versus OpenBLAS).
1. `artefact`: example of how to generate code at build time that is used as
   part of further build steps.
1. `openmp`: example of building an OpenMP application.
1. `mpi`: example of building an MPI application.
1. `hdf5`: example of building a Fortran application that uses HDF5.
1. `conan`: example of using the Conan C++ package manager.
1. `static_build`: example of an application that uses external libraries
   but which is build statically.
1. `static_boost`: example of an application that uses Boost Log and
   Filesystem and is statically linked.
1. `tbb`: example of building an application that uses TBB.
1. `mixed_code_scripts_install`: example of a project that contains
   C++ code for a shared libary and two executable, as well as a Python
   script and supporting modules.  Specifically illustrates installation
   of non-targets.
1. `templates`: example of installing a pure Python project that generates
   Bash wrapper scripts for each Python script from a common template.
1. `cuda`: example of how to build CUDA code.
1. `python-venv`: example of how to create a Python virtual environment
   that should be used at runtime to execute a Python script.  This includes
   a Bash script as a wrapper to enscapsulate the Python interpreter and
   dependencies.
1. `rpath`: illustration of how to build with RPATH.
1. `env_file`: illustration of how to create a file that contains content
   based on CMake variables during the build process.
1. `cython`: illustration of using CMake to build Cython extensions.
