'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''

class Solution:
    def majorityElement(self, nums:[int]) -> int:
        n = len(nums)
        a = {}
        b = c = nums[0]
        d = 0
        for i in range(0,n):
            if b > nums[i]:
                b = nums[i]
            if c < nums[i]:
                c = nums[i]
            a.setdefault(nums[i],0)
            a[nums[i]] += 1
        for i in range(b,c+1):
            index = a.get(i,0)
            if index > d:
                d = index
                if n/2 < d:
                    return i 

a = Solution()
print(a.majorityElement([3,2,3]))