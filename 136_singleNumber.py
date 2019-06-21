# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：

# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

class Solution:
    def singleNumber(self, nums:[int]) -> int:
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
            if dict.get(i,0) == 1:
                return i

a = Solution()
print(a.singleNumber([4,1,2,1,2]))