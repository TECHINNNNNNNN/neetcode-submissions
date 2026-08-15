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
            if (dupSet.has(s[r])){
                while (dupSet.has(s[r])){
                    dupSet.delete(s[l])
                    l += 1
                }
            } else {
                dupSet.add(s[r])
                maxLen = Math.max(maxLen, dupSet.size)
                r += 1
            }
        }

        return maxLen
    }
}
