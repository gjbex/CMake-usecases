# Templates

This project illustrates the installation of pure Python code, i.e.,
two scripts and a module as well as the generation of wrapper shell
scripts to conviniently run the scripts.

## What is it?

1. `scripts`: directory that contains the Python code.
  1. `hello.py`: script that will say hello to a given name.
  1. `bye.py`: script that will say bye to a given name.
  1. `utils/__init__.py`: make the directory a package.
  1. `utils/messages.py`: a module defining a utility function.
  1. `CMakeLists.txt`: CMake file that will install the scripts
     and the module, as well as generate wrapper Bash scripts
     for both Python scripts and install those as well.
1. `tmpl/run.tmpl`: the template for the Bash wrapper script, filled
   out by CMake's `configure_file` function.
1. `CMakeLists.txt`: top-level CMake file to generate the wrapper
   scripts and install the software.
