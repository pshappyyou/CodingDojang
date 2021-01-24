# 0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.
#
# sample inputs: 0123456789 01234 01234567890 6789012345 012322456789
#
# sample outputs: true false false true false


# inputNum = input("Enter the Number: ")
#
# if len(inputNum) != 10:
#     print("false")
# else:
#     for j in range(10):
#         cnt = 0
#         for i in range(len(inputNum)):
#             if int(inputNum[i]) == j:
#                 cnt = cnt+1
#
#         if cnt != 1 :
#             print("false")
#             break
#     print("true")

a = input("0~9 사이의 숫자로 이루어진 문자열 입력 : ")
print('true' if len(a) == len(set(a)) == 10  else 'false')