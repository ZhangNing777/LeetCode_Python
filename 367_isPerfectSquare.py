'''
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 4:
            return num == 1 or num == 4
        l, r = 0, num
        while l < r:
            mid = (l+r) // 2
            tmp = mid * mid
            if tmp == num:
                return True
            elif tmp < num:
                l = mid + 1
            else:
                r = mid
        return False
