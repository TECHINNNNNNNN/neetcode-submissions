class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = "".join(c.lower() for c in s if c.isalnum())
                
        
        for i in range(len(newS)):
            if  newS[i] != newS[len(newS) - 1 -i]:
                print(f"s[i] : {newS[i]}")
                print(f"s[len(s) - 1 - i] {newS[len(newS) - 1 - i]}")
                return False


        return True     