class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            L = 0
            R = len(matrix[i]) - 1
            while L <= R:
                m = L + (R - L) // 2
                if target < matrix[i][m]:
                    R = m - 1
                elif target > matrix[i][m]:
                    L = m + 1
                else :
                    return True
        
        return False