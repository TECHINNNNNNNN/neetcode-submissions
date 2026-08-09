class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixSumByRow = []
        
        for i in range(len(matrix)):
            prefixSum = []
            total = 0
            for j in range(len(matrix[0])):
                total += matrix[i][j]
                prefixSum.append(total)
            
            self.prefixSumByRow.append(prefixSum)




    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = 0
        print(self.prefixSumByRow)

        for i in range(row1, row2 + 1):
            prefixSum1 = self.prefixSumByRow[i][col2]
            prefixSum2 = self.prefixSumByRow[i][col1 - 1] if col1 > 0 else 0
            result += prefixSum1 - prefixSum2
        
        return result

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)