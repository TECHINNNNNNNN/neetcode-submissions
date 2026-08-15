class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestLength = 0

        numsSet = set(nums)

        for num in nums:
            if num - 1 not in numsSet:
                current = num
                length = 1
                while current + 1 in numsSet:
                    length += 1
                    current += 1
                
                longestLength = max(length, longestLength)






        return longestLength

        