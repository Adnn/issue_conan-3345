cmake_minimum_required (VERSION 3.0)

project (conan-test)

add_executable(${PROJECT_NAME} main.cpp)
install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION bin)
