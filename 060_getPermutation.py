'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:
输入: n = 3, k = 3
输出: "213"
示例 2:
输入: n = 4, k = 9
输出: "2314"
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return str(1)

        ans = [i+1 for i in range(n)]
        res = 0
        index = 1

        for i in range(n-1):
            index *= i+1

        while len(ans) > 2:
            a = k//index
            k %= index
            n -= 1
            index //= n
            if k == 0:
                a -= 1
            res = res*10 + ans[a]        
            ans.pop(a)
    
        if  k == 0 or k == 2:
            res = res*100 + ans[1]*10 + ans[0]
        else:
            res = res*100 + ans[0]*10 + ans[1]

        return str(res)

a = Solution()
print(a.getPermutation(4,12))