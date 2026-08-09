class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLength = min(len(w1),len(w2))

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            
            for j in range(minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        result = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True
            
            for neighbor in adj[char]:
                if dfs(neighbor):
                    return True
            
            visited[char] = False
            result.append(char)
            return False
        
        for char in adj:
            if dfs(char):
                return ""
        
        return "".join(reversed(result))

        