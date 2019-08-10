'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        res = 'aeiouAEIOU'
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if s[l] in res and s[r] in res:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in res:
                r -= 1
            elif s[r] in res:
                l += 1
            else:
                l += 1
                r -= 1
        res = ''.join(s)
        return res