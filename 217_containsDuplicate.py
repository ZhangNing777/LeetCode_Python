'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''

class Solution:
    def containsDuplicate(self, nums:[int]) -> bool:
        if len(nums) == 0:
            return False
        dict = {}
        a = b = nums[0]
        for i in range(0,len(nums)):
            if a > nums[i]:
                a = nums[i]
            elif b < nums[i]:
                b = nums[i]
            if dict.get(nums[i],None) == None:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        for i in range(a,b+1):
            if dict.get(i,None) >= 2:
                return True
        return False

a = Solution()
print(a.containsDuplicate([7,10,5,5,6,6,4,10,5,4,9,4,9,6,5,9,6,3,6,5,6,7,7,4,9,9,10,5,8,1,8,3,2,7,5,10,1,8,5,8,4,3,6,4,9,4,2,8,3,2,2,1,5,6,3,2,6,1,8,6,2,9,1,4,5,10,8,5,10,5,10,1,4,8,3,6,4,10,9,1,1,1,2,2,9,6,6,8,1,9,2,5,5,2,1,8,5,2,3,10]))