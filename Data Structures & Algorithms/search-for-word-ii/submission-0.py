class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visit = set()
        result = set()
        root = TrieNode()

        def insert(word):
            node = root  # Start at root
            for char in word:
                # If this character isn't in children, create it
                if char not in node.children:
                    node.children[char] = TrieNode()
                # Move to that child
                node = node.children[char]
            # Mark end of word
            node.isEndOfWord = True
        

        def dfs(row, col, node, path):  # node = current TrieNode, path = word built so far
            # Base cases (out of bounds, visited)
            if (row,col) in visit:
                return 
            
            if row == len(board) or col == len(board[0]) or row < 0 or col < 0:
                return

            char = board[row][col]

            # Is this char in the Trie?
            if char not in node.children:
                return
            
            visit.add((row,col))

            nextNode = node.children[char]
            path = path + char

            # Found a word?
            if nextNode.isEndOfWord:
                result.add(path)  # Add to result (use set to avoid duplicates)

            # Mark visited and explore 4 directions
            # ... backtracking logic ...
            dfs(row + 1, col, nextNode, path)
            dfs(row, col + 1, nextNode, path)
            dfs(row - 1, col, nextNode, path)
            dfs(row, col - 1, nextNode, path)

            visit.remove((row,col))

        for word in words:
            insert(word)


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, '')
            
        
        return list(result)
