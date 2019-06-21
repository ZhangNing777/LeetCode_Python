class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        length = len(s)
        sNew = []
        a = 2*numRows-2
        b = 0

        for i in range(0,numRows):
            index1 = i
            index2 = -1
            x = 0
            while index1 < length:
                if index1 != index2: 
                    sNew.append(s[index1])
                    index2 = index1
                if x == 0:
                    index1 += a
                    x = 1
                elif x == 1:
                    index1 += b
                    x = 0
            a -= 2
            b += 2

        return "".join(sNew)

a = Solution()

print(a.convert('PAYPALISHIRING', 3))