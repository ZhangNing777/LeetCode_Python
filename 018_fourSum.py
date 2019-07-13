'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        
        ans = {}
        n = len(nums)
        
        if n < 4:
            return ans
        
        nums.sort()
        
        for i in range(0,n-3):
            for j in range(i+1,n-2):
                left=j+1
                right=len(nums)-1
                
                while(right>left):
                    temp=nums[i]+nums[j]+nums[left]+nums[right]
                    if temp==target:
                        ans[nums[i],nums[j],nums[left],nums[right]]= nums[i],nums[j],nums[left],nums[right]
                        left+=1
                        right-=1
                    if temp>target:
                        right-=1
                    if temp<target:
                        left+=1

        result = []

        for i in ans:
            result.append(ans[i])
 

        return result

a = Solution()
print(a.fourSum([1,1,2,2,3,3,4,5,6,7,8,9],15))