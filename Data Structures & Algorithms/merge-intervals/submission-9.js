class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        let result = []
        intervals.sort((a, b) => a[0] - b[0])
        let start_interval = intervals[0][0]
        let end_interval = intervals[0][1]

        for (const interval of intervals.slice(1)){
            // [1, 3], [1, 5], [6, 7]
            if (interval[0] <= end_interval){
                end_interval = Math.max(end_interval, interval[1])
                start_interval = Math.min(start_interval, interval[0])
            } else {
                result.push([start_interval, end_interval])
                start_interval = interval[0]
                end_interval = interval[1]

            }

        }

        result.push([start_interval, end_interval])





        return result
    }
}
