class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l = 0
        r = len(heights) - 1
        maxLeft = heights[0]
        maxRight = heights[len(heights) - 1]
        water = 0

        while l < r:
            if maxLeft < maxRight:
                l += 1

                maxLeft = max(maxLeft, heights[l])
                water += maxLeft - heights[l]
            else:
                r -= 1

                maxRight = max(maxRight, heights[r])
                water += maxRight - heights[r]
            
        return water

        







        