set(catkin_virtualenv_CMAKE_DIR ${catkin_virtualenv_DIR})

# Include cmake modules from catkin_virtualenv
include(${catkin_virtualenv_CMAKE_DIR}/catkin_generate_virtualenv.cmake)
include(${catkin_virtualenv_CMAKE_DIR}/catkin_install_python.cmake)
