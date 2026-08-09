class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.append(stones[0])

        self.heap = stones
        cur = (len(self.heap) - 1) // 2

        while cur > 0:
            i = cur

            while 2*i < len(self.heap):
                if (2*i + 1 < len(self.heap)) and (self.heap[2*i + 1] > self.heap[2*i]) and (self.heap[2*i + 1] > self.heap[i]):
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i + 1]
                    self.heap[2*i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[2* i] > self.heap[i]:
                    tmp = self.heap[i] 
                    self.heap[i] = self.heap[2*i]
                    self.heap[2*i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
        print("original heap:", self.heap)
        
        while len(self.heap) > 2:
            most_heavy = self.pop(self.heap)
            almost_heavy = self.pop(self.heap)
            print("most_heavy: ", most_heavy)
            print("almost_heavy", almost_heavy)
            if most_heavy == almost_heavy:
                continue
            elif most_heavy != almost_heavy:
                self.push(self.heap,abs(most_heavy - almost_heavy))
            print("real time self.heap", self.heap)
        
        print(f"self.heap : {self.heap}")
        
        if len(self.heap) > 1:
            return self.heap[1]
        else :
            return 0
        
                
    

    def pop(self, arr):
        if len(arr) == 1:
            return 
        if len(arr) == 2:
            return arr.pop()

        res = arr[1]
        arr[1] = arr.pop()
        i = 1
        while 2*i <len(arr):
            if (2*i + 1) < len(arr) and arr[2*i + 1] > arr[2* i] and arr[2*i + 1] > arr[i]:
                tmp = arr[i]
                arr[i] = arr[2*i + 1]
                arr[2*i + 1] = tmp
                i = 2*i + 1
            elif arr[2*i] > arr[i]:
                tmp = arr[i]
                arr[i] = arr[2*i]
                arr[2*i] = tmp
                i = 2* i
            else:
                break
        print("pop value", res)
        return res
    
    def push(self, arr,val):
        arr.append(val)
        i = len(arr) - 1
        print("append value : ",val)

        while i > 1 and arr[i] > arr[i // 2]:
            tmp = arr[i]
            arr[i] = arr[i//2]
            arr[i//2] = tmp
            i = i // 2


        