class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}

        for char in s:
            if char not in word1:
                word1[char] = 0
            word1[char] += 1
        
        for c in t:
            if c in word1:
                if word1[c] == 0:
                    return False
                word1[c] -= 1
            else:
                return False
        if sum(word1.values()) == 0:
            return True
        
        return False


        