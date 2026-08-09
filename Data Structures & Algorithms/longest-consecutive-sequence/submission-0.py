class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        

        numsSet = set(nums)
        max_length = 0

        for n in numsSet:
            if (n - 1) not in numsSet:
                current_num = n
                current_length = 1


                while (current_num + 1) in numsSet:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
            
        