class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        rightProduct = 1

        for i in range(1,len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            rightProduct *= nums[i + 1]
            res[i] = res[i] * rightProduct

        
        return res

        