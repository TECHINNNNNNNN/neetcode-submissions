class Solution:
    def rob(self, nums: List[int]) -> int:

        return self.sumNotAdjacent(nums,0,{})
    
    def sumNotAdjacent(self, nums,i,cache):
        if i >= len(nums):
            return 0
        if i in cache:
            return cache[i]

        dontRob = self.sumNotAdjacent(nums,i + 1,cache)
        rob = nums[i] + self.sumNotAdjacent(nums, i + 2,cache)

        cache[i] = max(dontRob, rob)

        return cache[i]
        
            