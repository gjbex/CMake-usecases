# set minimal version for CMake
cmake_minimum_required(VERSION 3.0 FATAL_ERROR)

# project name and specifications
project(env_file LANGUAGES CXX)

# C++ compiler and C++ standard to use
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS NO)

# this project depends on GSL, find it.  Libraries will be in GSL::gsl and
# GSL::gslcblas
find_package(GSL REQUIRED)
if (NOT GSL_FOUND)
    message(FATAL_ERROR "GSL is required, but not found")
endif (NOT GSL_FOUND)

# add src subdirectory
add_subdirectory(src)

# create environment file
get_filename_component(gsl_lib_dir ${GSL_LIBRARY} DIRECTORY)
set(env_file_txt "# GSL library path\nexport LD_LIBRARY_PATH=\"${gsl_lib_dir}:$LD_LIBRARY_PATH\"\n")
set(env_file ${CMAKE_CURRENT_BINARY_DIR}/conf.sh)
file(WRITE "${env_file}" "${env_file_txt}")

# install generated environment file
install(FILES ${env_file} DESTINATION ${CMAKE_INSTALL_PREFIX}/conf)
