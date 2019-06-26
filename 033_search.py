'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''

class Solution:
    def search(self, nums:[int], target: int) -> int:
        n = len(nums)
        
        if n == 0:
            return -1
        
        if n == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
                
        a = 0
        b = n-1   

        if nums[0] > target and nums[n-1] < target:
            return -1

        if nums[a] == target:
            return a
            
        if nums[b] == target:
            return b


        while a!=b:
            if nums[a] > nums[b]:
                a = a+1
            else:
                b = b-1

        x = a

        a = 0
        b = n-1

        index = (a+b)//2

        if x == 0:
            if target < nums[0] or target > nums[n-1]:
                return -1
        
            while a < b:
                if nums[index] < target:
                    a = index+1
                else:
                    b = index
                index = (a+b)//2
                if nums[a] == target:
                    return a
                
            return -1


        if target < nums[x] or target > nums[x-1]:
            return -1
        elif target > nums[0]:
            a = 0
            b = x-1
        else:
            a = x
            b = n-1

        index = (a+b)//2
        while a < b:
            if nums[index] < target:
                a = index+1
            else:
                b = index
            index = (a+b)//2
            if nums[a] == target:
                    return a
                
        return -1

                


a = Solution()
print(a.search([4,5,6,7,8,9,1,2,3],1))