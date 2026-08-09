class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStart, resLen = 0, 0

        for i in range(len(s)):
            a, b, len1 = self.expand(i,i,s)
            c, d, len2 = self.expand(i, i + 1,s)

            if len1 > resLen:
                resStart, resLen = a, len1
            
            if len2 > resLen:
                resStart, resLen = c, len2
            
        
        return s[resStart: resStart + resLen]

    

    def expand(self, left, right,s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return left + 1, right - 1, right - left - 1

