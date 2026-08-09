class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = [[None] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        def helper(grid,i,j,cache):
            
            if i == len(grid) or j == len(grid[0]):
                return 0
            
            if grid[i][j] == 1:
                return 0
            
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return 1
            
            if cache[i][j]:
                return cache[i][j]

            cache[i][j] = helper(grid,i + 1,j,cache) + helper(grid, i , j + 1, cache)
            
            return cache[i][j]
        
        return helper(obstacleGrid,0,0,cache)
            

