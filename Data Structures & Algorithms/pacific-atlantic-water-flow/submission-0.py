class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []

        def canReachPacific(row,col,visited):
            if row == 0 or col == 0:
                return True

            visited.add((row,col))
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (0 <= nr < len(heights)) and (0 <= nc < len(heights[0])) and ((nr,nc) not in visited) and (heights[nr][nc] <= heights[row][col]):
                    if canReachPacific(nr,nc,visited):
                        return True
            
            return False
        
        def canReachAtlantic(row,col,visit):
            if row == len(heights) - 1 or col == len(heights[0]) - 1:
                return True
            
            visit.add((row,col))
            
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (0 <= nr < len(heights)) and (0 <= nc < len(heights[0])) and ((nr,nc) not in visit) and (heights[nr][nc] <= heights[row][col]):
                    if canReachAtlantic(nr,nc,visit):
                        return True
            
            return False
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if canReachPacific(i,j,set()) and canReachAtlantic(i,j,set()):
                    result.append([i,j])
        
        return result


            
        