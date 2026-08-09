class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # case 1 simple Kadane
        max_sum_case_1 = nums[0]
        cur_sum = 0

        for n in nums:
            cur_sum = max(cur_sum, 0)
            cur_sum += n
            max_sum_case_1 = max(max_sum_case_1, cur_sum)
        
        # case 2 inverse Kadane

        min_sum = nums[0]
        cur_min = 0

        for n in nums:
            cur_min = min(0, cur_min)
            cur_min += n 
            min_sum = min(min_sum, cur_min)
        
        case_2_sum = sum(nums) - min_sum

        if max_sum_case_1 < 0:
            return max_sum_case_1

        return max(max_sum_case_1, case_2_sum)
        

        