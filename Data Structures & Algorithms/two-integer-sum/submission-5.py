class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countSum = {}

        for i in range(len(nums)):
            if nums[i] in countSum:
                return [countSum[nums[i]] ,i]
            countSum[target - nums[i]] = i
        

        