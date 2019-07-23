'''
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        
        d1 = {}
        d2 = {}
        
        for i in range(0,l):
            if d1.get(s[i],None) == None:
                d1[s[i]] = i
                if d2.get(t[i],None) == None:
                    d2[t[i]] = i
                else:
                    return False
            else:
                if d1.get(s[i],None) == d2.get(t[i],None):
                    d1[s[i]] = i
                    d2[t[i]]= i
                else:
                    return False
                
        return True

a = Solution()
print(a.isIsomorphic("egg","add"))