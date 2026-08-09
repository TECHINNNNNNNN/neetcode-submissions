class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visit = set()
        def dfs(row,col,wordIndex):
            if row == ROW or col == COL or row < 0 or col < 0 :
                return False
            
            if (row,col) in visit:
                return False

            if word[wordIndex] != board[row][col]:
                return False
            
            visit.add((row,col))

            if wordIndex + 1 == len(word):
                return True

            result = dfs(row + 1,col,wordIndex + 1) or dfs(row,col + 1,wordIndex + 1) or dfs(row - 1,col,wordIndex + 1) or dfs(row,col - 1,wordIndex + 1)

            visit.remove((row,col))
            
            return result
        
        for i in range(ROW):
            for j in range(COL):
                if dfs(i,j,0):
                    return True
        
        return False
