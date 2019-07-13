'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums:[int], target: int) -> int:
        n = len(nums)
        if n < 3:
            return False
            
        c = nums[0]+nums[1]+nums[2]
        index = abs(c-target)
        
        nums.sort()
        
        for i in range(1,n-1):
            a = 0
            b = n-1
            while a < i and i < b:
                s = nums[a] + nums[i] + nums[b]
                if abs(s-target) < index:
                    index = abs(s-target)
                    c = s
                if s > target:
                    b -= 1
                elif s < target:
                    a += 1
                elif s == target:
                    return c
                
        return c