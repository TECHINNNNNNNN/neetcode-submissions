class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        
        top, bottom = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while top <= bottom and l <= r:

            for i in range(l, r + 1):
                result.append(matrix[top][i])
            
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][r])
            
            r -= 1

            if top > bottom or l > r:
                break
            
            for i in range(r, l - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][l])
            l += 1
        
        return result
