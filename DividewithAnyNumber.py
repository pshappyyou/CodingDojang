# 1부터 10까지의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
#
# 그렇다면 1부터 20까지의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?



# num =0
# for i in range(11, 100000000):
#     for j in range(1,21):
#         if i%j != 0 :
#             break
#         else:
#             if j == 20:
#                 num = i
#     if num > 0:
#         break
#
# print("i: {0}".format(i))
# print("num: {0}".format(num))


elem=[2]
for i in range(3,20):
    for j in range(2,i):
        if i%j==0:
            break
        elif j==i-1:
            elem.append(i)

ans=1
for i in elem:
    while 1:
        if i*i>20:
            ans*=i
            break
        i*=i

print(ans)