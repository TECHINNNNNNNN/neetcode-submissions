/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {number}
     */
    minMeetingRooms(intervals) {
        const start = intervals.map((i) => i.start).sort((a, b) => a - b)
        const end = intervals.map((i) => i.end).sort((a, b) => a - b)
        // [0,5,15] , [10, 20, 40]
        let maxSchedule = 0
        let startPointer = 0
        let endPointer = 0 
        let count = 0

        while (startPointer < intervals.length && endPointer < intervals.length){
            if (start[startPointer] < end[endPointer]){
                count += 1
                maxSchedule = Math.max(maxSchedule, count)
                startPointer += 1
            } else {
                count -= 1
                endPointer += 1
            }
        }

        return maxSchedule
    }
}