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
1. `testing`: example of using CTest.
1. `doxygen`: example of generating doxygen documentation.
1. `clang_tidy`: example of invoking clang-tidy during the build process.
1. `blas_lapack/`: example of using BLAS and Lapack, as well as specifying
   a specific BLAS/LAPACK implementation (i.e., MKL versus OpenBLAS).
1. `artefact`: example of how to generate code at build time that is used as
   part of further build steps.
1. `openmp`: example of building an OpenMP application.
1. `mpi`: example of building an MPI application.
1. `hdf5`: example of building a Fortran application that uses HDF5.
