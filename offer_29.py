'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 
限制：
0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = []
        
        a = len(matrix)
        
        if a == 0:
            return l

        b = len(matrix[0])
        c = -1
        d = -2
        
       
        m = [0, 1, 0, -1]
        n = [1, 0, -1, 0]
        
        x = y = z = 0
        
        index = a*b
        
        while len(l) < index:
            
            l.append(matrix[y][z])
            y += m[x]
            z += n[x]

            if c < y < a and d < z < b:
                continue
            else:
                y -= m[x]
                z -= n[x]
                

                if x == 1:
                    d += 1
                elif x == 2:
                    a -= 1
                elif x == 3:
                    b -= 1
                else:
                    c += 1
                    
                x = (x+1)%4
                y += m[x]
                z += n[x]

        return l