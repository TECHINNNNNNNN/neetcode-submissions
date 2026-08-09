class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        def helper(i, prev):
            if i == len(nums):
                return 0
            
            skip = helper(i + 1, prev)

            take = 0
            if nums[i] > prev:
                take = 1 + helper(i + 1, nums[i])
            

            return max(take, skip)
        
        return helper(0, float('-inf'))


        