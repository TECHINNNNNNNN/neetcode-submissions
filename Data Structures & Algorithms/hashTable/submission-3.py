class Pair:
    def __init__(self,key,value):
        self.key = key
        self.val = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map = [None] * self.capacity
    
    def hash(self,key):
        return key % self.capacity


    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key,value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].val = value
                return
            index += 1
            index = index % self.capacity

    def get(self, key: int) -> int:
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        
        return -1



    def remove(self, key: int) -> bool:
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return True
            index += 1
            index = index % self.capacity
        
        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity = self.capacity * 2
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)
        
        oldMap = self.map
        self.map = newMap
        self.size = 0

        for pair in oldMap:
            if pair:
                self.insert(pair.key,pair.val)

