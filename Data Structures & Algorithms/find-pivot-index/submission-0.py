class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix = []

        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        

        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 0
            right = prefix[len(nums) - 1] - prefix[i]
            if right == left:
                return i
        
        return -1 

        