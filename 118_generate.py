'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [1]
        b = []
        c = []
        for index in range(numRows):
            b.append(1)
            for i in range(0, len(a)-1):
                b[i+1] = a[i] + a[i+1]
            c.append(b[:])
            a = b.copy()
        return c

a = Solution()
print(a.generate(4))