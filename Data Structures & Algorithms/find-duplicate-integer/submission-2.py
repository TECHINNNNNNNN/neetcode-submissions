class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = nums[0]
        f = nums[0]

        s = nums[s]
        f = nums[nums[f]]

        while s != f:
            s = nums[s]
            f = nums[nums[f]]
        
        s1 = nums[0]
        while s != s1:
            s = nums[s]
            s1 = nums[s1]
        
        return s
                

