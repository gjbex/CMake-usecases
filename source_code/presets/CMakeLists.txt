cmake_minimum_required(VERSION 3.20)

project(hello LANGUAGES CXX)

include(CTest)

add_executable(hello src/main.cpp)

if(BUILD_TESTING)
    add_test(NAME hello_runs COMMAND hello)
endif()
