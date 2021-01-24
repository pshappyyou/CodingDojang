# 앞의 문제들 중 비슷한 알고리즘이 있던 것 같지만, 같은 건 없다고 생각해서 올립니다. 문제를 푸는데 많은 approach가 있을 듯 싶습니다. 이 문제의 핵심은 비트 연산을 얼마나 잘 이해하고 있냐이기 때문에 비트 연산으로 풀어주세요.
#
# input은 int n을 입력 받아 첫번째 row는 (n-1)의 O와 X, 두번째 row는 (n-2)의 O와 XX, 세번째 row는 (n-3)의 0와 XXX... n번째 row는 n의 X을 출력하시오.
#
# 입력 예시: 6
#
# 출력 예시:
#
# OOOOOX
#
# OOOOXX
#
# OOOXXX
#
# OOXXXX
#
# OXXXXX
#
# XXXXXX


# n = input("Enter the number: ")
# listV = []
# o = 'O'
# x = "X"
# setV = set()
#
# for i in range(int(n)):
#     if i == int(n)-1:
#         listV.append(x)
#         setV.add(set(listV))
#     else:
#         listV.append(o)
#
# print(listV)
# print(setV)

# n = int(input())
# tmp = 2**n-1
# for i in range(n):
#     print(bin(tmp<<(i+1))[-n:].replace('1','O').replace('0','X'))

# print((lambda n: '\n'.join('O'*(n-i) + 'X'*i for i in range(1,n+1)))(int(input('>>>'))))


# b = ['X' for i in range(int(input("자연수 입력 : ")))]
# # print(b)
# # print(''.join(b))
# # print(b[:-1])
# # b[:-1] = 'O' * (len(b)-1)
# # print(''.join(b))
#
# for i in range(len(b)):
#     b[:-i-1] = 'O' * (len(b)-i-1)
# #    b[-i-1:] = 'X' * (i + 1)
#     print(''.join(b))

# for i, x in enumerate(b):
#     b[:-i-1] = 'O' * (len(b)-i-1)
#     b[-i-1:] = 'X' * (i + 1)
#     print(''.join(b))

# n = int(input('input n : '))
#
# for i in range(1, n+1):
#     print('O'*(n-i) + 'X'*i)

n = int(input("n을 입력하세요 : "))
# n = 6

print('\n'.join(["O" * (n - i - 1) + "X" * (i + 1) for i in range(n)]))