class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        
        def helper(s,i):

            if i in cache:
                return cache[i]

            if i == len(s):
                return True
            
            for w in wordDict:
                if s[i:].startswith(w):
                    if helper(s, i + len(w)):
                        cache[i] = True
                        return True
            
            cache[i] = False
            return False
        
        return helper(s, 0)