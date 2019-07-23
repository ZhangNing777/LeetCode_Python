'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        a = [0]*n
        b = 0
        
        for i in range(2,n):
            if a[i] == 0:
                b += 1
                for j in range(i,n,i):
                    a[j] = 1
        
        return b

a = Solution()
print(a.countPrimes(10))