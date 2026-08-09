class MinStack:

    def __init__(self):
        self.capacity = 10
        self.length = 0
        self.min_arr_length = 0
        self.arr = [0] * self.capacity
        self.min_arr = [0] * self.capacity
        

    def push(self, val: int) -> None:
        if self.length < self.capacity:
            self.arr[self.length] = val
            if self.length == 0:
                self.min_arr[0] = val
                self.min_arr_length += 1
            elif val <= self.min_arr[self.min_arr_length - 1]:
                self.min_arr[self.min_arr_length] = val
                self.min_arr_length += 1
            self.length += 1

        else :
            self.capacity *= 2
            new_arr = [0] * self.capacity
            new_min_arr = [0] * self.capacity
            for i in range(self.length):
                new_arr[i] = self.arr[i]
                new_min_arr[i] = self.min_arr[i]
            self.arr = new_arr 
            self.arr[self.length] = val
            if val <= self.arr[self.min_arr_length - 1]:
                self.min_arr[self.min_arr_length] = val
                self.min_arr_length += 1
            self.length += 1
        
        

    def pop(self) -> None:
        if self.min_arr[self.min_arr_length - 1] == self.arr[self.length - 1]:
            self.min_arr_length -= 1
        self.length -= 1
        

    def top(self) -> int:
        return self.arr[self.length - 1]
        

    def getMin(self) -> int:
        return self.min_arr[self.min_arr_length - 1]
        
        
