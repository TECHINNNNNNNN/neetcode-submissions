class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float('inf')
        L = 0
        total = 0

        for R in range(len(nums)):
            total += nums[R]

            while total >= target:
                min_length = min(min_length, R - L + 1)
                total -= nums[L]
                L += 1
        

        return min_length if min_length != float('inf') else 0

        