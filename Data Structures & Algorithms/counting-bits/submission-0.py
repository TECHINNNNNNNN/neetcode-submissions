class Solution:
    def countBits(self, n: int) -> List[int]:
        def helper(n):
            res = 0
            while n:
                n = n & (n-1)
                res +=1
            
            return res
        output = []
        
        for i in range(n + 1):
            output.append(helper(i))
        
        return output
        