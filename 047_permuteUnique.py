'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        check = [0 for i in range(len(nums))]
        ans = []
        def backtrack(a,n):
            if n == len(nums):
                ans.append(a.copy())
                return
            else:
                for i in range(len(nums)):
                    if check[i] == 1:
                        continue
                    elif i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                        continue
                    else:
                        a.append(nums[i])
                        check[i] = 1
                        backtrack(a,n+1)
                        a.pop()
                        check[i] = 0

        backtrack([],0)
        return ans

a = Solution()
print(a.permuteUnique([1,1,2]))