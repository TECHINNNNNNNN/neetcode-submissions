class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.append(points[0])
        result = []

        self.heap = points
        cur = (len(self.heap) - 1) // 2

        while cur > 0:
            i = cur
            while 2*i < len(self.heap):
                if (2 * i + 1 < len(self.heap)) and math.hypot(self.heap[2*i + 1][0], self.heap[2*i + 1][1]) < math.hypot(self.heap[2*i][0], self.heap[2*i][1]) and math.hypot(self.heap[i][0], self.heap[i][1]) > math.hypot(self.heap[2*i + 1][0], self.heap[2*i + 1][1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif sum(self.heap[i]) > sum(self.heap[2 * i]):
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
        
        for i in range(k):
            result.append(self.pop(self.heap))
        
        return result
        
    
    def pop(self,arr):
        if len(arr) == 1:
            return
        if len(arr) == 2:
            return arr.pop()
        

        res = arr[1]
        arr[1] = arr.pop()
        i = 1

        while 2*i < len(arr):
            print(f"i in loop pop: {i}")
            if (2*i + 1 < len(arr)) and math.hypot(arr[2*i + 1][0], arr[2*i + 1][1]) < math.hypot(arr[2*i][0], arr[2*i][1]) and math.hypot(arr[2*i + 1][0], arr[2*i + 1][1]) < math.hypot(arr[i][0], arr[i][1]):
                tmp = arr[i]
                arr[i] = arr[2*i + 1]
                arr[2*i + 1] = tmp
                i = 2*i + 1
            elif math.hypot(arr[2*i][0], arr[2*i][1]) < math.hypot(arr[i][0], arr[i][1]):
                tmp = arr[i]
                arr[i] = arr[2*i]
                arr[2*i] = tmp
                i = 2*i
            else:
                break
        
        return res
            

        