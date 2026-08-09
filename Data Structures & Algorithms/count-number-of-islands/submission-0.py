class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visit:
                    count += 1
                    self.islandHelper(grid,i,j,visit)
        return count
    
    def islandHelper(self,grid,r,c,visit):
        ROW, COL = len(grid), len(grid[0])
        if (min(int(r),int(c)) < 0) or r == ROW or c == COL or (r,c) in visit or grid[r][c] == '0':
            return
        
        visit.add((r,c))
        self.islandHelper(grid,r+1,c,visit)
        self.islandHelper(grid,r-1,c,visit)
        self.islandHelper(grid,r,c+1,visit)
        self.islandHelper(grid,r,c-1,visit)

        