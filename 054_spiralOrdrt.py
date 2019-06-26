class Solution:
    def spiralOrder(self, matrix:[[int]]) ->[int]:
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

a = Solution()
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))