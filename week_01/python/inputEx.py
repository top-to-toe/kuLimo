def main():  # main() 함수 정의 시작
    input_var = input("숫자를 입력하세요: ")  # 사용자로부터 입력을 받습니다. 입력은 항상 문자열(string)로 반환됩니다.
    print(f"입력한 숫자는 {input_var} 입니다.")  # 사용자가 입력한 값을 그대로 출력합니다.

    # 사용자가 입력한 값을 정수로 변환하여 30을 곱한 후 출력합니다.
    print(f"곱하기 30은: {int(input_var) * 30}")  # 입력된 문자열을 int()를 사용해 정수로 변환하고, 그 값을 30과 곱한 후 출력합니다.

if __name__ == "__main__":  # 이 파일이 직접 실행되었을 때만 아래 코드를 실행하도록 합니다.
    main()  # main() 함수를 호출하여 프로그램을 실행합니다.
