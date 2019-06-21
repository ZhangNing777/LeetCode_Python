'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

'''
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        list1 = nums1 + nums2
        list1.sort()
        x = len(nums1) + len(nums2)
        y = x/2
        if x%2 == 0:
            a = list1[y]
            b = list1[y]
            z = (a+b)/2
        else:
            z = list1[y-0.5]
            
        return z




    
S = Solution()

print(S.findMedianSortedArrays([1,5,9,11],[2,4,5,8,10,23]))