class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.check(s[i:j + 1]):
                    count += 1
        

        return count
        
    
    def check(self,ss):
        for i in range(len(ss)):
            if ss[i] != ss[len(ss) - 1 - i]:
                return False
        

        return True