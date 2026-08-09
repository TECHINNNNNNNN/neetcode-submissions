class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        lastPost = len(self.arr) - 1
        if len(self.arr) % 2 == 0:
            firstMed = int((lastPost / 2.0) - 0.5)
            secondMed = int((lastPost / 2.0) + 0.5)
            return (self.arr[firstMed] + self.arr[secondMed]) / 2.0
        else:
            return self.arr[int(lastPost / 2.0)]
        
        