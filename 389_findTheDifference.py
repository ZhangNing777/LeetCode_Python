'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

 

示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        l1 = len(s)
        l2 = len(t)
        
        d = {}
        
        for i in range(0,l1):
            if d.get(s[i]) != None:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
                
        for i in range(0,l2):
            if d.get(t[i]) == None:
                return t[i]
            elif d.get(t[i]) != None:
                d[t[i]] -= 1
                if d[t[i]] == -1:
                    return t[i]
                