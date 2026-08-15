class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freqDict = {}

        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1

        for keyNum in freqDict:
            heapq.heappush(heap, (freqDict[keyNum], keyNum))
            if len(heap) > k:
                heapq.heappop(heap)
      
        return [v for n,v in heap]

        