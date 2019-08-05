'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = len(s)
        l2 = len(t)
        
        if l1 != l2:
            return False
        
        d = {}
        
        for i in range(0,l1):
            if d.get(s[i]) != None:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
                
        for i in range(0,l2):
            if d.get(t[i]) == None:
                return False
            elif d.get(t[i]) != None:
                d[t[i]] -= 1
                if d[t[i]] < 0:
                    return False
                
        return True
                