class Solution:
    def numDecodings(self, s: str) -> int:

        def helper(i):

            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            

            ways = helper(i + 1)

            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6') :
                ways += helper(i + 2)
            
            return ways

        
        return helper(0)

        