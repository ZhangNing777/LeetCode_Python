'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31−1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

'''

class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        
        if x < 0:
            index = -1
            x *= -1
        else:
            index = 1

        y = 0

        while x != 0:
            a = x%10
            y = y*10 + a
            x //= 10

        y *= index

        if -2**31< y <2**31-1:
            return y
        return 0

a = Solution()
print(a.reverse(123456))