class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        max_count = 0
        def dfs(grid,i,j,visit):
            if (min(i,j) < 0 or i == ROW or j == COL or (i,j) in visit or grid[i][j] == 0):
                return 0
            visit.add((i,j))

            count = 1

            count += dfs(grid,i+1,j,visit)
            count += dfs(grid,i-1,j,visit)
            count += dfs(grid,i,j+1,visit)
            count += dfs(grid,i,j-1,visit)
            return count

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visit:
                    possible_new_high = dfs(grid,i,j,visit)
                    max_count = max(possible_new_high,max_count)
        return max_count

        