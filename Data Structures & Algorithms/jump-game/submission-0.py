class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def helper(index):
            if index >= len(nums) - 1:
                return True
        
            for i in range(1,nums[index] + 1):
                if helper(index + i):
                    return True
            

            return False
        
        return helper(0)
            
