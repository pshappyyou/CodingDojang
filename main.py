# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# A씨는 게시판 프로그램을 작성하고 있다.
#
# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.
#
# 입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
# 출력 : 총페이지수
#
# A씨가 필요한 프로그램을 작성하시오.
#
# 예) 프로그램 수행 시 다음과 같은 결과값이 나와야 함.
#
# m	n	출력
# 0	1	0
# 1	1	1
# 2	1	2
# 1	10	1
# 10	10	1
# 11	10	2

import keyboard

# while True:
#
#     m = int(input("Enter M value: "))
#     n = int(input("Enter N value: "))
#
#     if n < 1:
#         print("N value should bigger than 0")
#         continue
#
#     remain = m % n
#     output = round(m / n)
#     if remain > 0:
#         output = output + 1
#     print(m, n, output)
#

import math
#
# m = int(input('총건수: '))
# n = int(input('한페이지에 보여줄 게시물수: '))
#
print(math.ceil(m/n))

print(math.floor(m/n))
