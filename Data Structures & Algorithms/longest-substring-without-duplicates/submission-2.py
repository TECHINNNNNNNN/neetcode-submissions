class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        l, r = 0, 0

        dupSet = set()

        while r < len(s):
            if s[r] in dupSet:
                while s[r] in dupSet:
                    dupSet.remove(s[l])
                    l += 1
            else:
                dupSet.add(s[r])
                longestLength = max(len(dupSet), longestLength )
                r += 1
        
        return longestLength

        