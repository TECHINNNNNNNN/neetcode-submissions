class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float('-inf')

        for i in range(len(heights)):
            for j in range(len(heights)):
                width = abs(j - i)
                height = min(heights[j], heights[i])
                area = width * height

                max_area = max(area, max_area)




        return max_area
        