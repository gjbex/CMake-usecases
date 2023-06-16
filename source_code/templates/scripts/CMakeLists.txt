file(GLOB python_scripts "${CMAKE_CURRENT_SOURCE_DIR}/*.py")
set(template_bash_script "${CMAKE_CURRENT_SOURCE_DIR}/../tmpl/run.tmpl")
foreach(python_script ${python_scripts})
    get_filename_component(bash_script_name ${python_script} NAME_WE)
    get_filename_component(python_script_name ${python_script} NAME)
    install(FILES ${python_script_name} TYPE LIB)
    set(wrapper_file_name "${CMAKE_CURRENT_BINARY_DIR}/${bash_script_name}")
    configure_file(${template_bash_script} ${wrapper_file_name} @ONLY)
    set(target "wrapper_script_${bash_script_name}")
    add_custom_target(${target} ALL DEPENDS ${wrapper_file_name})
    install(PROGRAMS ${wrapper_file_name} DESTINATION bin)
endforeach()

install(DIRECTORY utils TYPE LIB
    PATTERN "*~" EXCLUDE
    PATTERN "*.bak" EXCLUDE
    PATTERN "__pycache__" EXCLUDE)
