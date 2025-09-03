cmake_minimum_required(VERSION 3.20)

project(failure LANGUAGES C)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_EXTENSIONS OFF)

add_executable(compute.exe compute.c)
target_compile_options(compute.exe PRIVATE -Wall -Wextra -Wpedantic)
target_link_libraries(compute.exe m)

add_executable(segfault.exe segfault.c)

add_executable(non_zero_exit.exe non_zero_exit.c)

include(CTest)

add_test(
    NAME compute_test1
    COMMAND compute.exe
)

add_test(
    NAME compute_test2
    COMMAND compute.exe 1.0 0.0
)
set_tests_properties(compute_test2
    PROPERTIES PASS_REGULAR_EXPRESSION "42.0"
)

add_test(
    NAME compute_test3
    COMMAND compute.exe -4.0 2.0
)
set_tests_properties(compute_test3
    PROPERTIES PASS_REGULAR_EXPRESSION "2.0i"
)

add_test(
    NAME compute_test4
    COMMAND compute.exe abc def
)
set_tests_properties(compute_test4
    PROPERTIES PASS_REGULAR_EXPRESSION "2.0i"
)

add_test(
    NAME segfault_test
    COMMAND segfault.exe
)

add_test(
    NAME non_zero_exit_test
    COMMAND non_zero_exit.exe
)

add_test(
    NAME non_zero_exit_test_wrapped
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/test_wrapper.sh $<TARGET_FILE:non_zero_exit.exe>
)

add_test(
    NAME timeout_test
    COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/test_wrapper.sh sleep 10
)
set_tests_properties(timeout_test PROPERTIES TIMEOUT 3)
