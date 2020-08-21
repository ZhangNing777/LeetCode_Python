'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]'''


# class Solution:
#     def permute(self, nums:[int]) ->[[int]]:
        
#         def backtrack(a = 0):
            
#             if a == n:  
#                 output.append(nums[:])
            
#             for i in range(a, n):
#                 nums[a], nums[i] = nums[i], nums[a]
#                 backtrack(a + 1)
#                 nums[a], nums[i] = nums[i], nums[a]
        
#         n = len(nums)
#         output = []
#         backtrack()
        
#         return output

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(a,n):
            if n == len(nums):
                res.append(a.copy())
                return
            else:
                for i in range(len(nums)):
                    if nums[i] not in a:
                        a.append(nums[i])
                        backtrack(a,n+1)
                        a.pop()

        backtrack([],0)
        return res

a = Solution()
print(a.permute([1,2,3]))