class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        badRow = set()
        badCol = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    badRow.add(i)
                    badCol.add(j)
        

        for row in badRow:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        
        for col in badCol:
            for k in range(len(matrix)):
                matrix[k][col] = 0
        



        
        
        
        