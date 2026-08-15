class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        
        noSyntaxString = ''

        for c in s:
            if c.isalnum():
                noSyntaxString += c
        
        right = len(noSyntaxString) - 1



        while left < right:
            if noSyntaxString[left].lower() != noSyntaxString[right].lower():
                return False
            left += 1
            right -= 1
            
        
        return True
        
        