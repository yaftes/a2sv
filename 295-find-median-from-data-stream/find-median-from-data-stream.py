class MedianFinder:

    def __init__(self):
        self.median = list()

    def addNum(self, num: int) -> None:
        self.median.append(num)
        
    def findMedian(self) -> float:
        self.median.sort()
        length = len(self.median)
        if length > 0:
            if length % 2 == 0:
                return (self.median[(length//2)-1] + self.median[length//2]) / 2
            else:
                return self.median[length//2]
        return -1


         