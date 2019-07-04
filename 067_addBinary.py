'''给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = int(a) +int(b)
        n = 0
        index = 1
        y = 0
        
        while m != 0:
            x = m%10
            if x >= 2:
                x -= 2
                y = 1
                
            n += x*index
            
            m = m//10 + y
            y = 0
            index = index*10
            
        return str(n)
            
a = Solution()
print(a.addBinary("11","1"))