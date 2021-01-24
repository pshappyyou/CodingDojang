# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자. 출처
#
# 입력 - 화면에서 숫자로 된 문자열을 입력받는다.
# "4546793"
# 출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
# "454*67-9-3"




# str= "4546793"
# newlist= list(str)
#
# print(newlist)
# oddcnt = 0
# evencnt = 0
# for i in range(len(newlist)):
#
#     if int(newlist[i]) % 2 == 0:
#         if evencnt > 0:
#             newlist.insert(i, "*")
#             evencnt = 0
#
#         else:
#             evencnt += 1
#             oddcnt =0
#     else:
#         if oddcnt > 0:
#             newlist.insert(i, "-")
#             oddcnt = 0
#             evencnt = 0
#         else:
#             oddcnt += 1
#             evencnt=0
#
# print(''.join(newlist))

# i = list(map(int,' '.join(input()).split()))

string = "4546793"
i = list(map(int,string))
print(i)
answer=[str(i[0])]
print(answer)

for x in range(len(i)-1):
    if i[x] %2 ==0 and i[x+1]%2==0:
        answer.append("*")
    if i[x]%2==1 and i[x+1]%2==1:
        answer.append("-")
    answer.append(str(i[x+1]))

print(''.join(answer))

# answer = [str(i[0])]
# for x in range(len(i)-1):
#     if i[x]%2==0 and i[x+1]%2==0:
#         answer.append('*')
#     if i[x]%2==1 and i[x+1]%2==1:
#         answer.append('-')
#     answer.append(str(i[x+1]))
# print(''.join(answer))