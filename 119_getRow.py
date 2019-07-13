'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [1]
        b = []
        for index in range(rowIndex+1):
            b.append(1)
            for i in range(0, len(a)-1):
                b[i+1] = a[i] + a[i+1]
            a = b.copy()
        return b