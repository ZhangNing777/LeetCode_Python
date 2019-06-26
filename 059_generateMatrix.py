'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l = [[0 for i in range(n)] for g in range(n)]
        
        index = 1
        
        a = b = n
        c = -1
        d = -2
        e = n*n
        
       
        m = [0, 1, 0, -1]
        n = [1, 0, -1, 0]
        
        x = y = z = 0
        
        while index <= e:
            l[y][z] = index
            index += 1
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