class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(nums,i,cache):
            if i >= len(nums):
                return 0
            
            if cache[i] != None:
                return cache[i]

            rob = nums[i] + helper(nums,i + 2,cache)
            dontRob = helper(nums, i + 1,cache)
            
            cache[i] = max(rob,dontRob)
            return cache[i]
        
        cache1 = [None] * (len(nums) - 1)
        cache2 = [None] * (len(nums) - 1)
        
        return max(helper(nums[0:len(nums)- 1],0,cache1),helper(nums[1:],0,cache2))
        