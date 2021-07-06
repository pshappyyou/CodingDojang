# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
# Example 4:

# Input: x = 0
# Output: 0
 

# Constraints:

# -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            strg = str(x)
            if x >= 0 :
                revst = strg[::-1]
            else:
                temp = strg[1:] 
                temp2 = temp[::-1] 
                revst = "-" + temp2
            if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
            else: return int(revst)

class Test:
    def swap(self, x):
        print(x[1:])
        print(x[::-1])

a = Solution()
ret = a.reverse(-123)
print(ret)

b = Test()
b.swap([1,2,3,4,5,6,7])