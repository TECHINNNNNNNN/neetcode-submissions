class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = self.multArr(nums[:i] + nums[i + 1:])
        
        return res
    

    def multArr(self,arr):
        result = 1

        for num in arr:
            result *= num
        
        return result

        