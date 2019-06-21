class Solution:
    def removeDuplicates(self, nums:[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1

a = Solution()
l1 = [1,1,2]
len = a.removeDuplicates(l1)

print(l1[:len])

