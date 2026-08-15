class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxWater = 0
        let l = 0
        let r = heights.length - 1

        while (l < r){
            const water = Math.min(heights[l], heights[r]) * (r - l)
            maxWater = Math.max(water, maxWater)

            if (heights[l] < heights[r]){
                l += 1
            } else if (heights[l] > heights[r]){
                r -= 1
            } else{
                l += 1
            }
        }




        return maxWater
    }
}
