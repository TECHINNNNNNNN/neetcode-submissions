class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [None] * len(nums)
        def helper(index,cache):
            if index >= len(nums) - 1:
                cache[index] = True
                return True
        
            for i in range(1,nums[index] + 1):
                if cache[index] == True:
                    return True
                elif helper(index + i,cache):
                    return True

            cache[index] = False
            return cache[index]
        
        return helper(0,cache)
            
