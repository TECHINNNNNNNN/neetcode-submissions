class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            pivot = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right and left < len(nums) and right < len(nums):
                if nums[left] + nums[right] == -pivot:
                    result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > -pivot:
                    right -= 1
                else:
                    left += 1
            
        
        return [list(x) for x in set(tuple(sorted(x)) for x in result)]


        