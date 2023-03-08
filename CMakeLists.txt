cmake_minimum_required(VERSION 3.3)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_CXX_COMPILER clang++)

project(
    projectName
    VERSION 1.0
    DESCRIPTION "project description"
)

add_executable(projectName main.cpp)
