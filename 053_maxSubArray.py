'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

class Solution:
    def maxSubArray(self, nums:[int]) -> int:
        a = b = nums[0]
        for i in range(1,len(nums)):
            if a + nums[i]>nums[i]:
                b = max(b, a+nums[i])
                a += nums[i]
            else:
                b = max(b, a, a+nums[i], nums[i])
                a = nums[i]
        return b

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))