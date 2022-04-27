# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "kondo_webots: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ikondo_webots:/home/tndrd/workspaces/kondo/src/kondo_webots/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(kondo_webots_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg" NAME_WE)
add_custom_target(_kondo_webots_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "kondo_webots" "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(kondo_webots
  "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kondo_webots
)

### Generating Services

### Generating Module File
_generate_module_cpp(kondo_webots
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kondo_webots
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(kondo_webots_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(kondo_webots_generate_messages kondo_webots_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg" NAME_WE)
add_dependencies(kondo_webots_generate_messages_cpp _kondo_webots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kondo_webots_gencpp)
add_dependencies(kondo_webots_gencpp kondo_webots_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kondo_webots_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(kondo_webots
  "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kondo_webots
)

### Generating Services

### Generating Module File
_generate_module_eus(kondo_webots
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kondo_webots
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(kondo_webots_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(kondo_webots_generate_messages kondo_webots_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg" NAME_WE)
add_dependencies(kondo_webots_generate_messages_eus _kondo_webots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kondo_webots_geneus)
add_dependencies(kondo_webots_geneus kondo_webots_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kondo_webots_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(kondo_webots
  "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kondo_webots
)

### Generating Services

### Generating Module File
_generate_module_lisp(kondo_webots
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kondo_webots
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(kondo_webots_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(kondo_webots_generate_messages kondo_webots_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg" NAME_WE)
add_dependencies(kondo_webots_generate_messages_lisp _kondo_webots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kondo_webots_genlisp)
add_dependencies(kondo_webots_genlisp kondo_webots_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kondo_webots_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(kondo_webots
  "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kondo_webots
)

### Generating Services

### Generating Module File
_generate_module_nodejs(kondo_webots
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kondo_webots
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(kondo_webots_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(kondo_webots_generate_messages kondo_webots_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg" NAME_WE)
add_dependencies(kondo_webots_generate_messages_nodejs _kondo_webots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kondo_webots_gennodejs)
add_dependencies(kondo_webots_gennodejs kondo_webots_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kondo_webots_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(kondo_webots
  "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kondo_webots
)

### Generating Services

### Generating Module File
_generate_module_py(kondo_webots
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kondo_webots
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(kondo_webots_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(kondo_webots_generate_messages kondo_webots_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tndrd/workspaces/kondo/src/kondo_webots/msg/servo_command.msg" NAME_WE)
add_dependencies(kondo_webots_generate_messages_py _kondo_webots_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(kondo_webots_genpy)
add_dependencies(kondo_webots_genpy kondo_webots_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS kondo_webots_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kondo_webots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/kondo_webots
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(kondo_webots_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kondo_webots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/kondo_webots
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(kondo_webots_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kondo_webots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/kondo_webots
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(kondo_webots_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kondo_webots)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/kondo_webots
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(kondo_webots_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kondo_webots)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kondo_webots\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/kondo_webots
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(kondo_webots_generate_messages_py std_msgs_generate_messages_py)
endif()
