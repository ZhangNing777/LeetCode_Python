'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

class Solution:
    def threeSum(self, nums:[int]) -> [int]:
        a = []
        n = len(nums)
        if n <3:
            return a
        
        
        
        nums.sort()
        index = 0
        

        for i in range(1,n-1):
            if nums[1] == nums[-2]:
                if nums[0] + nums[-1] + nums[1] == 0:
                    a.append((nums[0],nums[1],nums[-1]))
                    return a
            else:
                left = 0
                right = n-1
                while left < i and i < right:
                    if nums[left] + nums[i] + nums[right] == 0:
                        if nums[i] != nums[i+1] or right-1 == i: 
                            a.append((nums[left],nums[i],nums[right]))
                        right -= 1
                        left += 1
                        while nums[right] == nums[right+1]:
                            right -= 1
                        while nums[left] == nums[left-1]:
                            left += 1
                    elif nums[left] + nums[i] + nums[right] > 0:
                        right -= 1
                    elif nums[left] + nums[i] + nums[right] < 0:
                        left += 1
            
        return a


a = Solution()
print(a.threeSum([-2,0,1,1,2]))