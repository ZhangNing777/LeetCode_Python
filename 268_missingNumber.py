'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        nums.append(-1)
        l = len(nums)
        index = l-1

        for i in range(0,l):
            

            while nums[i] != i:
                if i == index:
                    return index
                if nums[i] == -1:
                    a = nums[i]
                    nums[i] = nums[index]
                    nums[index] = a
                else:
                    a = nums[i]
                    nums[i] = nums[a]
                    nums[a] = a
                    if a == index:
                        index -= 1
        

a=Solution()
print(a.missingNumber([0,4,6,7,3,2,1,9,8]))