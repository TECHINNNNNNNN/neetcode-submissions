class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.usage = []
        self.data = {}
        

    def get(self, key: int) -> int:
        print("self.data when get:", self.data)
        if key in self.data:
            if key in self.usage:
                self.usage.remove(key)
            self.usage.append(key)
            return self.data[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key] = value
            self.usage.remove(key)
            self.usage.append(key)
            return
        
        if len(self.data) == self.capacity:
            lru_key = self.usage.pop(0)
            del self.data[lru_key]
        
        self.data[key] = value
        self.usage.append(key)

        
