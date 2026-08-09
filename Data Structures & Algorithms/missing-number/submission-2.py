class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        data = set()

        for n in nums:
            data.add(n)

        
        for i in range(len(nums) + 1):
            if i not in data:
                return i
    
        