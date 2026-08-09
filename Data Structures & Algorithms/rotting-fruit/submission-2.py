class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid),len(grid[0])
        allFruit = 0
        visit = set()
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visit.add((i,j))
                    allFruit += 1
                elif grid[i][j] == 1:
                    allFruit += 1
        
        duration = 0

        while queue:
            print("queue: ", queue)
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr,c + dc) in visit or grid[r + dr][c + dc] == 0 or grid[r + dr][c + dc] == 2):
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                
            duration += 1

        print(f"allFruit: {allFruit} , visit: {visit}")
        print(f"len(visit) = {len(visit)}")
        
        if len(visit) < allFruit:
            return -1

        if duration > 0 :
            return duration - 1
        
        return 0
                


        