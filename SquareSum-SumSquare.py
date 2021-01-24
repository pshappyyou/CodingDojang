# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다
# (제곱의 합). 1^2 + 2^2 + ... + 10^2 = 385
# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다
# (합의 제곱). (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.
# 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?



listNum=list(i for i in range(1,101))

Sum1 = 0
Sum2 = 0

for x in listNum:
    Sum1 = Sum1 + (x**2)
    Sum2 = Sum2 + x

Sum2 = Sum2**2
print("The difference of Square of Sum minus Sum of Square of each number is {0}".format(Sum2-Sum1))

###
sum_of_squares=sum(x**2 for x in range(1,101))
square_of_sums=sum(range(1,100))**2
print(sum_of_squares)
print(square_of_sums)
print(abs(sum_of_squares-square_of_sums))

####
print(abs(sum(range(1, 101))**2 - sum(x**2 for x in range(1, 101))))