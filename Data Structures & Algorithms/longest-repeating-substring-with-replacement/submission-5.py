class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 1
        l, r = 0, 0

        freqMap = {}
        while r < len(s):
            freqMap[s[r]] = freqMap.get(s[r], 0) + 1
            while r - l + 1 - max(freqMap.values()) > k:
                freqMap[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
            r += 1
           
            








        return maxLength
        