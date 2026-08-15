class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):
            pivot = nums[i]

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < -pivot:
                    left += 1
                elif nums[left] + nums[right] > -pivot:
                    right -= 1
                elif nums[left] + nums[right] == -pivot:
                    result.append([pivot, nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1 
                    right -= 1
        

        return result



        