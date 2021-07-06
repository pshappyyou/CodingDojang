class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el!= 0 :
                nums[pos], nums[i] = nums[i], nums[pos]
                pos=pos+1
        return nums

a=Solution()
answer=a.moveZeroes([0,1,0,3,12])
print(answer)


class Solution2(object):
    def moveZeroes(self, nums):
        append_times=nums.count(1)
        for i in range(append_times):
            nums.remove(0) #  Delete the front zero
            nums.append(0)
        return nums

a=Solution2()
answer=a.moveZeroes([0,1,0,3,12])
print(answer)    