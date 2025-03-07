cmake_minimum_required(VERSION 3.8) # 빌드에 필요한 최소 cmake 버전

project(cmake_example) # 프로젝트 이름

# 실행 파일
add_executable(cmake_example src/cmake_example.cpp) # main 함수가 있는 코드 

include_directories("include") # include 디렉토리를 포함

add_library(AddNumber src/add_number.cpp) # 라이브러리 추가

add_executable(add_num src/add_main.cpp) # 실행 파일

Target_link_libraries(add_num AddNumber) # 실행 파일에 라이브러리 링크