class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortLength = [len(s), len(s) * 2]
        current = {}
        l, r = 0, 0
        tDict = Counter(t)
        need = len(tDict)
        have = 0

        while r < len(s):
            current[s[r]] = current.get(s[r], 0) + 1
            if s[r] in tDict and current[s[r]] == tDict[s[r]]:
                have += 1
            while have >= need:
                if (r - l + 1 < shortLength[1] - shortLength[0] + 1):
                    shortLength = [l, r]
                current[s[l]] -= 1
                if s[l] in tDict and current[s[l]] < tDict[s[l]]:
                    have -= 1
                l += 1
            
            r += 1

         
        return  s[shortLength[0]: shortLength[1] + 1] if shortLength[1] != len(s) * 2  else ""


    
    
        




        