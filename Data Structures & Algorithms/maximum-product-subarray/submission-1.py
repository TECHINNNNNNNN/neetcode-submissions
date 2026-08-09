class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for n in nums:
            temp_max = max(n, n * curMax, n * curMin)
            curMin = min(n, n * curMax, n * curMin)
            curMax = temp_max

            if curMax > res:
                res = curMax
        
        return res

