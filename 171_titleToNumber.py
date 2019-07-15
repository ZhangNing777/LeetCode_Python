'''
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        a = 0
        l = len(s)
        b = 26**(l-1)
        for i in range(l):
            index = ord(s[i]) - 64
            a += index * b
            b = b//26
        return a

a = Solution()
print(a.titleToNumber('AAA'))