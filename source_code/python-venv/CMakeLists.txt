cmake_minimum_required(VERSION 3.10)

project(python_venv)

# find Python 3.x
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# create virtual environment
execute_process(COMMAND ${Python3_EXECUTABLE} -m venv ${CMAKE_CURRENT_BINARY_DIR}/venv)

# set virtual environment as active
set(ENV{VIRTUAL_ENV} ${CMAKE_CURRENT_BINARY_DIR}/venv)

# find Python 3.x again, this time in the virtual environment
unset(Python3_EXECUTABLE)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# upgrade pip, setuptools and wheel
execute_process(COMMAND ${CMAKE_CURRENT_BINARY_DIR}/venv/bin/pip install --upgrade pip)
execute_process(COMMAND ${CMAKE_CURRENT_BINARY_DIR}/venv/bin/pip install --upgrade setuptools)
execute_process(COMMAND ${CMAKE_CURRENT_BINARY_DIR}/venv/bin/pip install --upgrade wheel)

# install package from requirements.txt
execute_process(COMMAND ${CMAKE_CURRENT_BINARY_DIR}/venv/bin/pip install -r ${CMAKE_CURRENT_SOURCE_DIR}/requirements.txt)

# add installation target that copies the virtual environment
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/venv DESTINATION ${CMAKE_INSTALL_PREFIX})

# add install target for the Python script that should be stored in the lib directory
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/avg.py DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)

# add install target for the Bash wrapper script that should be stored in the bin directory
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/avg
    DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
    PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)
