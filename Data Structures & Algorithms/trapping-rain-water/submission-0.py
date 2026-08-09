class Solution:
    def trap(self, heights: List[int]) -> int:
        maxLeft = [0] * len(heights)
        maxRight = [0] * len(heights)

        maxLeft[0] = heights[0]
        maxRight[len(heights) - 1] = heights[len(heights) - 1]


        for i in range(1,len(heights)):
            maxLeft[i] = max(heights[i], maxLeft[i - 1])

        for i in range(len(heights) - 2, -1, -1):
            maxRight[i] = max(heights[i], maxRight[i + 1])

        
        trappedWater = 0

        for i in range(1,len(heights) - 1):
            trappedWater += min(maxLeft[i], maxRight[i]) - heights[i]

        
        return trappedWater

        

        







        