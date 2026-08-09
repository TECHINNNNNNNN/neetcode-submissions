class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expandFromCenter(left, right):
            result = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            return result

        for i in range(len(s)):
            count += expandFromCenter(i,i)
            count += expandFromCenter(i,i + 1)
        
        return count