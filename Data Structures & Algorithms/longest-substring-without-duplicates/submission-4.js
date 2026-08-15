class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let maxLen = 0
        let l = 0
        let r = 0
        let dupSet = new Set()

        while ( r < s.length ){
            while (dupSet.has(s[r])){
                dupSet.delete(s[l])
                l += 1
            }
            dupSet.add(s[r])
            maxLen = Math.max(maxLen, r - l + 1)
            r += 1
        }

        return maxLen
    }
}
