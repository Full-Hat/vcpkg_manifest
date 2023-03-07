cmake_minimum_required(VERSION 3.3)

set(CMAKE_CXX_STANDARD 20)

set(CMAKE_CXX_COMPILER clang++)

#set(CMAKE_TOOLCHAIN_FILE "${CMAKE_CURRENT_SOURCE_DIR}/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")

project(
    projectName
    VERSION 1.0
    DESCRIPTION "project description"
)

add_executable(projectName main.cpp)

find_package(unofficial-sqlite3 CONFIG REQUIRED)
target_link_libraries(projectName PRIVATE unofficial::sqlite3::sqlite3)

find_package(SQLiteCpp CONFIG REQUIRED)
target_link_libraries(projectName PRIVATE SQLiteCpp)

#find_package(unofficial-sqlite3 CONFIG REQUIRED)

#target_link_libraries(main PRIVATE unofficial::sqlite3::sqlite3)
