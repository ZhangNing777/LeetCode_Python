'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s)
        index = 0
        a = 0
        
        for i in range(l-1,-1,-1):
            if s[i] == ' ':
                index += 1
            else:
                break
                
        for i in range(l-index-1,-1,-1):
            if s[i] == ' ':
                break
            else:
                a += 1

        return a