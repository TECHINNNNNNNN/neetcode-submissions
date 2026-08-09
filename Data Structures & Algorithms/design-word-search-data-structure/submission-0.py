class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            
            current = current.children[char]
        
        current.isEndOfWord = True
        return 

    def search(self, word: str) -> bool:
        return self.helper(word,0,self.root)

    def helper(self, word,index ,node):
        if index == len(word):
            return node.isEndOfWord
        
        char = word[index]

        if char == ".":
            for child in node.children.values():
               if self.helper(word, index + 1, child):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self.helper(word, index + 1, node.children[char])
            

            
        
        
