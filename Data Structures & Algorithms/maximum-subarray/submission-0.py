class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')

        def helper(i, current_sum):
            nonlocal max_sum


            if i >= len(nums):
                return
            
            current_sum = max(nums[i], nums[i] + current_sum)

            max_sum = max(max_sum, current_sum)
            helper(i + 1, current_sum)

        helper(0,0)

        return max_sum


        