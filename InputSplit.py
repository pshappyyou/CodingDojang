# 프로그램 실행 순서
#
# 입력할 정수의 개수를 사용자로부터 입력 받는다.
# 입력받은 정수의 개수만큼 정수를 입력받는다.
# 입력받은 정수의 합과 평균 값을 출력한다.
# 할당된 메모리공간을 비운다.
#
# 요구사항
#
# 메모리공간은 사용자의 입력 수의 따라 변동된다.
# 사용한 공간은 마지막에 비워야 한다.
# 배열을 사용하면 안된다.

#n_list = list(map(int, input("Enter number(s): ").split()))

n = int(input("Enter number of input: "))

inputList =[]

for i in range(n):
    inputList.append(int(input("{0} 번째 숫자 입력: ".format(i+1))))

print("전체 숫자 합은 {0} 입니다.".format(sum(inputList)))
print("전체 숫자 평균은 {0} 입니다.".format(sum(inputList)/n))
inputList.clear()

