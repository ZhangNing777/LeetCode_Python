from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(a,candidates,target):
            if target == 0:
                ans.append(a.copy())
                return
            else:
                for i in range(len(candidates)):
                    if candidates[i] <= target:
                        a.append(candidates[i])
                        backtrack(a, candidates[i:len(candidates)], target-candidates[i])
                        a.pop()
                    
        
        backtrack([], candidates, target)
        return ans
                    

a = Solution()
print(a.combinationSum([2,3,7],7))