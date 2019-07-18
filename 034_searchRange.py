'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0:
            return [-1,-1]
        
        left = 0
        right  = len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                left = mid
                right = mid
                
        
        if nums[left] == nums[right] == target: 
            while left > 0:
                if nums[left-1] == target:
                    left -= 1
                else:
                    break
                        
            while right < len(nums)-1:
                if nums[right+1] == target:
                    right += 1
                else:
                    break

            return left,right
        else:
            return [-1,-1]

a = Solution()
print(a.searchRange([1,1],2))