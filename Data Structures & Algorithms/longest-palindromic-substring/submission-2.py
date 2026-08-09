class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = [0, (0,0)]
        
        for i in range(len(s)):
            p = self.checkPalindrome(s,i)
            if p[0] > result[0]:
                result[1] = p[1]
                result[0] = p[0]
        begin,ending = result[1]
        return s[begin:ending + 1]
        
        

    
    def checkPalindrome(self,s, index):
        left = index
        right = index
        result = [0, (0,0)]

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > result[0]:
                result[1] = [left, right]
                result[0] = right - left + 1
            right += 1
            left -= 1
        
        l = index
        r = index + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > result[0]:
                result[1] = [l, r]
                result[0] = r - l + 1
            r += 1
            l -= 1
        
        return result


