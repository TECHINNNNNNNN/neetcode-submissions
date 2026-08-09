class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(1,len(nums)):
            left[i] *= nums[i - 1] * left[i - 1]
            right[len(nums) - 1 - i] *= nums[len(nums) - i] * right[len(nums) - i]
            print(left)
            print(right)
        
        return [a * b for a,b in zip(left,right)]

        