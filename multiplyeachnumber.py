# 예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
#
# 10 = 1 * 0 = 0
# 11 = 1 * 1 = 1
# 12 = 1 * 2 = 2
# 13 = 1 * 3 = 3
# 14 = 1 * 4 = 4
# 15 = 1 * 5 = 5
#
# 그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15




# q=[ for x in range(10,1000)]

# Result =1
# Totalsum =0
#
# for i in range(10,1001):
#     for x in str(i):
#         Result *= int(x)
#     Totalsum += Result
#     Result =1
#
# print("TotalSum: {0}".format(Totalsum))

# num = []
# for i in range(10,1000+1):
#     s = list(str(i))
#     s = '*'.join(s)
#     num.append(eval(s))
# print(sum(num))


print(sum([eval('*'.join(str(i))) for i in range(10, 1001)]))