cmake_minimum_required(VERSION 3.0.2)
project(better_teleop)

find_package(catkin REQUIRED)

catkin_package()

include_directories()

catkin_install_python(
    PROGRAMS
    scripts/better_teleop.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
