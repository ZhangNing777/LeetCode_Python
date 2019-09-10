'''
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.
'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        
        for i in nums:
            if d.get(i,0) == 0:
                d[i] = 1
            else:
                d[i] += 1
                
        index = 0
            
        for i in d:
            if d.get(i+1,0) != 0:
                if d[i] + d[i+1] > index:
                    index = d[i] + d[i+1]
        
        return index
