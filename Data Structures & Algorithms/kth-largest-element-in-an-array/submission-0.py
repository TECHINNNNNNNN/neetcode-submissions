import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-s for s in nums]
        print(neg_nums)
        heapq.heapify(neg_nums)
        while k > 1:
            heapq.heappop(neg_nums)
            k -= 1
        
        return -heapq.heappop(neg_nums)