# CMake presets

This project is a simple illustration of how to use CMake presets. It defines
two presets: `debug` and `release`, which can be used to build the project in
debug or release mode, respectively.


## What is it?

1. `CMakePresets.json` defines the presets for configuring and building the project.
1. `src/main.cpp` is the source code for the project, which simply prints
   "Hello, World!" to the console.
1. `CMakeLists.txt` is the CMake configuration file that defines how to build the
   project.


## How to use it?

To list all the available presets, run the following command in the terminal:

```bash
$ cmake  --list-presets
```

To configure the project using a specific preset, use the `--preset` option:

```bash
$ cmake  --preset debug
```

To build the project using a specific preset, use the `--preset` option with the
`--build` command:

```bash
$ cmake  --build  --preset debug
```
