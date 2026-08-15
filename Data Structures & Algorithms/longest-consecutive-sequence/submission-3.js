class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const numsSet = new Set(nums)
        let maxLength = 0

        for (const n of numsSet){
            if (!numsSet.has(n - 1)){
                let length = 1
                let current = 1
                while (numsSet.has(n + current)){
                    length += 1
                    current += 1
                }

                maxLength = Math.max(maxLength, length)
            }
        }

        return maxLength
    }
}
