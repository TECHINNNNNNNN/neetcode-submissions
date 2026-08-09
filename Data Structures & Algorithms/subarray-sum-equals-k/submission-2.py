class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixMap = {0: 1}
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            prefixSum = currentSum - k
            count += prefixMap.get(prefixSum,0)
            if currentSum not in prefixMap:
                prefixMap[currentSum] = 0
            prefixMap[currentSum] += 1
            
        return count