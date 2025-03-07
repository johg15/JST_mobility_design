#include "add_number.hpp" // 사용할 함수가 선언된 헤더파일

int main(int argc, char *argv[] ) {

    if(argc < 3) {
        std::cout<<"Usage: "<<argv[0]<<" num1 num2 "<<std::endl;  // 실행파일 실행 시 숫자 두개를 받았는지 확인
        return 1;
    }
    double num1 = atof(argv[1]);
    double num2 = atof(argv[2]);
    double result = add(num1, num2); // add_number에 정의된 함수 사용

    std::cout<<"Result: "<<num1<<"+"<<num2<<" = "<<result<<std::endl; // 결과 출력
    return 0;

}