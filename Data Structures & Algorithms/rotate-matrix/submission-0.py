class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 1 :
            return matrix
        up = 0 
        down = len(matrix) - 1

        while up < down:
            tmp = matrix[up]
            matrix[up] = matrix[down]
            matrix[down] = tmp
            up += 1
            down -= 1
        
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        