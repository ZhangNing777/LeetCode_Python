class Solution:
    def removeElement(self, nums:[int], val: int) -> int:
        index = -1
        for i in range(0, len(nums)):
            if nums[i] != val:
                index += 1
                nums[index] = nums[i]
        return index + 1

a = Solution()
l1 = [2,1,1,2,]
len = a.removeElement(l1,2)

print(l1[:len])