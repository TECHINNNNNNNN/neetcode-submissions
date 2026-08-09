class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        output = []


        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            bucket[value].append(key)
        
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] != []:
                for num in bucket[i]:
                    if k > 0:
                        output.append(num)
                        k -= 1
        return output


