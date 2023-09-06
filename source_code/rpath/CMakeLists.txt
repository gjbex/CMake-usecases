cmake_minimum_required(VERSION 3.10)

project(globals LANGUAGES C)

option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")

add_library(globals SHARED
    global.c
    global.h
    context1.c
    context1.h
    context2.c
    context2.h
)

target_include_directories(globals PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(globals_test
    main.c
)

target_link_libraries(globals_test PUBLIC globals)

install(TARGETS globals DESTINATION lib)
install(FILES global.h context1.h context2.h DESTINATION include)
install(TARGETS globals_test DESTINATION bin)
