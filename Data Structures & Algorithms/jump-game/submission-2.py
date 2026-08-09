class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [None] * len(nums)
        def helper(index,cache):
            if index >= len(nums) - 1:
                return True
            
            if cache[index] is not None:
                return cache[index]
        
            for i in range(1,nums[index] + 1):
                if helper(index + i,cache):
                    cache[index] =True
                    return True

            cache[index] = False
            return cache[index]
        
        return helper(0,cache)
            
