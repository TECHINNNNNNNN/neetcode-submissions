class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countSum = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            countSum[complement] = i

        for i in range(len(nums)):
            if nums[i] in countSum and countSum[nums[i]] != i:
                return [i, countSum[nums[i]]]
        
        
        
     

        