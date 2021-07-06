class Solution:
    def twoSum(self, nums, target) :
        for x in range(0, len(nums)-1):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return x, y
                


if __name__ == '__main__':
    a = Solution()
    print(a.twoSum([6,2,4],6))