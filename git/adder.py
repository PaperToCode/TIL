# 두 값을 정수로 합을 계산하는 함수

def add(x:int, y:int)-> int:

    return int(x)+int(y)

print(add(5,3))

print(add("5","3"))


def main():

    num1= input("첫번째 숫자를 입력해주세요:")

    num2= input("두번째 숫자를 입력해주세요:")


    result = add(num1,num2)

    print(f"두 숫자의 합은 {result}입니다.")


# 파일이 직접 실행될 때에만 코드 실행.

if __name__ == "__main__":

    main()
    
