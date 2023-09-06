# python-env

Example of how to create a Python virtual environment to use from
a Bash wrapper script to encapsulate all dependencies that are
available in the virtual environment, including the Python
interpreter itself.


## What is it?

1. `avg.py`: Python script that imports pandas to read a CSV file,
   and computes the mean value for each column it considers numerical.
1. `avg`: Bash script to activate the virtual environment that
   constains the Python interpreter, the pandas library and its
   dependencies.
1. `requirements.txt`: Python packages to be installed in the virtual
   environment.
1. `CMakeLists.txt`: CMake file to build and install this utility.
1. `data.csv`: CSV data file to experiment with.
