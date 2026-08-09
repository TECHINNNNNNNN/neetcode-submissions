class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else :
                count[nums[i]] += 1

        sorted_count = dict(sorted(count.items(), key=lambda item:item[1],reverse=True))
        
        j = 0
        for key, value in sorted_count.items():
            j += 1
            res.append(key)

            if j == k:
                break

        

        return res