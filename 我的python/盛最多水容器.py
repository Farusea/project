class Solution:
    def maxArea(self, height):
        temp = 0
        left = 0
        right = len(height)-1
        while left < right:
            temp = max(temp, (right-left)*min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return temp

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
f = Solution()
print(f.maxArea(height))