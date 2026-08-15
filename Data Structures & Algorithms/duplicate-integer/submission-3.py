class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numberBucket = set()

        for num in nums:
            if num in numberBucket:
                return True
            numberBucket.add(num)
        
        return False