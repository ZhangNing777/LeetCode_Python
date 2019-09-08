class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        a = len(nums)
        b = len(nums[0])
        
        if a * b != c * r:
            return nums
        
        m = []
        n = []
        
        for i in range(a):
            for j in range(b):
                m.append(nums[i][j])
                if len(m) == c:
                    n.append(m)
                    m = []
        return n
