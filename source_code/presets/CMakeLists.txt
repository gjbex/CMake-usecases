cmake_minimum_required(VERSION 3.20)

project(hello LANGUAGES CXX)

include(CTest)

option(ENABLE_GPROF "Build with gprof instrumentation" OFF)
option(ENABLE_SANITIZERS "Build with AddressSanitizer and UndefinedBehaviorSanitizer" OFF)

add_executable(hello src/main.cpp)

if(ENABLE_GPROF)
    target_compile_options(hello PRIVATE
        $<$<CXX_COMPILER_ID:GNU>:-pg>
    )
    target_link_options(hello PRIVATE
        $<$<CXX_COMPILER_ID:GNU>:-pg>
    )
endif()

if(ENABLE_SANITIZERS)
    target_compile_options(hello PRIVATE
        $<$<CXX_COMPILER_ID:GNU,Clang,AppleClang>:-fsanitize=address,undefined>
        $<$<CXX_COMPILER_ID:GNU,Clang,AppleClang>:-fno-omit-frame-pointer>
    )
    target_link_options(hello PRIVATE
        $<$<CXX_COMPILER_ID:GNU,Clang,AppleClang>:-fsanitize=address,undefined>
    )
endif()

if(BUILD_TESTING)
    add_test(NAME hello_runs COMMAND hello)
endif()
