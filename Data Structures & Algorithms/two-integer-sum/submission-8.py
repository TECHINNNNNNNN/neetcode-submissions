class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmpDict = {}

        for index in range(len(nums)):
            if nums[index] not in tmpDict:
                tmpDict[target - nums[index]] = index
            else:
                return [tmpDict[nums[index]], index]
        