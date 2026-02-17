# FetchContent

You can fetch and build the content of a third-party library using CMake's
`FetchContent` module.  This allows you to include the library as part of your
build process without having to manually download and install it.


## What is it?

1. `random_default.cpp`: A simple example of using CLI11 to parse command line
   arguments.
1. `CMakeLists.txt`: CMake file to build the example.  CMake will automatically
   download and include CLI11 as a dependency.
