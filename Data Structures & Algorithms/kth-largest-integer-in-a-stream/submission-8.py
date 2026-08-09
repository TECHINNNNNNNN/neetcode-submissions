class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []

        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            self.heap.append(val)
            i = len(self.heap) - 1
            while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
                self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
                i = (i - 1) // 2 # Move up to the parent's index
        elif val > self.heap[0]:
            self.heap[0] = val

            i = 0

            while 2 * i + 1 < len(self.heap):
                if (2*i + 2) < len(self.heap) and self.heap[2 * i + 2] < self.heap[2 * i + 1] and self.heap[i] > self.heap[2*i+2]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 2]
                    self.heap[2 * i + 2] = tmp
                    i = 2 * i + 2
                elif self.heap[i] > self.heap[2 * i + 1]:
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i + 1]
                    self.heap[2*i + 1] = tmp
                    i = 2 * i + 1
                else:
                    break
            
        return self.heap[0]




        
