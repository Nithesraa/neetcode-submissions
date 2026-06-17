class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        n = len(matrix)
        m = len(matrix[0])
        l , r = 0 , (n*m) - 1
        while l <= r:
            mid = (l+r)//2
            row , col = divmod(mid,m)
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            elif mid_val < target:
                l+=1
            elif mid_val > target:
                r-=1
        return False