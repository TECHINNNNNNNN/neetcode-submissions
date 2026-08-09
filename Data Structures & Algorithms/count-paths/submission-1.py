class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for i in range(m)]
        def helper(m,n,row,col,cache):
            if row == m or col == n:
                return 0
            
            if row == m - 1 and col == n-1:
                return 1
            
            if cache[row][col] != 0:
                return cache[row][col]
            
            cache[row][col] = helper(m,n,row + 1, col,cache) + helper(m,n,row,col + 1,cache)
            return cache[row][col]
        
        return helper(m,n,0,0,cache)