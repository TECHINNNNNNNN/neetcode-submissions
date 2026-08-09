class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = [[None] * len(text2) for i in range(len(text1))]
        def helper(text1, text2, i,j,cache):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                if cache[i][j] != None:
                    return cache[i][j]
                cache[i][j] = 1 + helper(text1,text2,i + 1, j + 1,cache)
                return cache[i][j]
            else:
                if cache[i][j] != None:
                    return cache[i][j]
                cache[i][j] =  max(helper(text1,text2,i + 1,j,cache),helper(text1,text2,i,j + 1,cache))
                return cache[i][j]
    
        return helper(text1,text2,0,0,cache)