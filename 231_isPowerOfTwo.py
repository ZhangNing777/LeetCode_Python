'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        
        if n == 1:
            return True
        elif n%2 != 0:
            return False
        else:
            self.isPowerOfTwo(n//2)

a = Solution()
print(a.isPowerOfTwo(2))