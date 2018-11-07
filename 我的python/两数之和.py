class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    L = [i, j]
                    print(L)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
sum = Solution()
sum.twoSum(nums, target)