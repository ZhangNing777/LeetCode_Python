'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。
'''

class Solution:
    def maxProfit(self, prices: [int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        a = prices[0]
        b = 0
        for i in range(1,n):
            if a > prices[i]:
                a = prices[i]
            if prices[i] - a > b:
                b = prices[i] - a
        return b

a = Solution()
print(a.maxProfit([1,3,5,3,6,5]))
            

 

