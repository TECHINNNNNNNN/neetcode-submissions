class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let maxLength = 0
        let freqMap = {}
        let l = 0
        let r = 0

        while (r < s.length){
            freqMap[s[r]] = (freqMap[s[r]] || 0) + 1
            while (r - l + 1 - Math.max(...Object.values(freqMap)) > k){
                freqMap[s[l]] -= 1
                l += 1
            }
            maxLength = Math.max(maxLength, r - l +1)
            r += 1
        }

        




        return maxLength 
    }
}
