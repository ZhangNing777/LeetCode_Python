class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = ["()", "[]", "{}"]
        for i in range(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2]+stack[-1] in d:
                stack.pop()
                stack.pop()
        return len(stack) == 0

a = Solution()

print(a.isValid("{([])}"))