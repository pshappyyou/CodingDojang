# Input
#
# 테스트 케이스의 개수에는 제한이 없으며, 각 테스트 케이스마다 삼각형의 세 변의 길이를 나타내는 실수 세 개(a,b,c)가 입력된다.
# 어떤 변의 길이도 1,000,000을 넘지 않으며, max(a,b,c) ≤ (a+b+c)/2 라고 가정해도 된다.
#
# 파일 끝에 다다를 때까지 계속 입력을 받는다.
#
# output
#
# 각 테스트 케이스마다 다음과 같은 결과를 출력한다.
#
# The radius of the round table is: r
# 여기에서 r은 정오에 해가 비추는 영역에 들어갈 수 있는 원탁의 최대 반지름이며, 소수점 셋째 자리까지 반올림한 값을 출력한다.
#
# Sample Input
#
# 12.0 12.0 8.0
# Sample Output
#
# The radius of the round table is: 2.828

# a,b,c = input("Enter three values by space: ").split()
#
# float(a)
# float(b)
# float(c)
#
# if a > 1000000 or b >1000000 or c> 1000000:
#     print("please enter number smaller than 1000000")
#     break
#
#
# print(a,b,c)

# from math import *
#
# while True:
#     inp = input("Enter three values: ")
#     if len(inp.split()) != 3:
#         break
#     a,b,c = map(float,inp.split())
#     s = (a+b+c)/2
#     heron = sqrt(s*(s-a)*(s-b)*(s-c))
#     r = heron/s # 1/s = 2/(a+b+c)
#     print('The radius of the round table is: {0:.3f}'.format(r))


import math

num = list(map(float,input().split(' ')))
p = sum(num)/2
S = math.sqrt(p*(p-num[0])*(p-num[1])*(p-num[2]))
print(round(S/p,3))


'''
s = (a+b+c)/2,
S = sqrt( s(s-a)(s-b)(s-c) ) = 1/2 * r * (a+b+c) = s * r
=> r = S / s
'''

with open("input.txt", "r") as f:
    a, b, c = map(float, f.readline().split())
    s = (a + b + c) / 2
    S = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    r = S / s
    print("The radius of the round table is: ", round(r, 3))