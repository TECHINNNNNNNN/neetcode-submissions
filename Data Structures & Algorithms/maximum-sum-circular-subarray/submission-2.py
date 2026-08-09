class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max, global_max = 0, nums[0]
        cur_min, global_min = 0 , nums[0]


        for n in nums:
            cur_max = max(cur_max,0)
            cur_max += n
            global_max = max(global_max,cur_max)


            cur_min = min(0, cur_min)
            cur_min += n
            global_min = min(global_min, cur_min)
        

        if global_max < 0:
            return global_max
        
        return max(global_max,sum(nums) - global_min)
        

        