# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         if n<2:
#             return s
#         left = 0
#         right = n
#         a = b = c = 0
         
#         for i in range(0 , n):
#             for j in range(0 , n-i):
#                 if s[i] == s[n-j-1]:
#                     x = i
#                     z = j
#                     bool1 = 1
#                     c = 0
#                     while x + z < n-1:
#                         x += 1
#                         z += 1
#                         c += 1
#                         if s[x] != s[n-z-1]:
#                             bool1 = 0
#                             break
#                         else:
#                             bool1 = 1

#                     bool2 = 0

#                     if bool1 == 1:
#                         a = i
#                         b = j
#                         bool2 = 1

#                     if bool2 == 1:
#                         if b+a < right+left:
#                             left = a
#                             right = b
#                             bool2 = 0

#         if left + right == n:
#             return s[0]
#         else:
#             return s[left:n-right]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        n = len(s)
        for i in range(n - 1):
            if 2 * (n - i) + 1 < right - left + 1:
                break
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 2 > right - left:
                left = l + 1
                right = r - 1
        return s[left:right + 1]


a = Solution()

print(a.longestPalindrome("asdfdcd"))
