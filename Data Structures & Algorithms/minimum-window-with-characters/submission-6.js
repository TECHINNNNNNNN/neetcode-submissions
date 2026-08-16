class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {string}
     */
    minWindow(s, t) {
        let resStart = 0
        let resLen = s.length + 1
        let l = 0
        let r = 0
        const tDict = [...t].reduce((acc, char) => {
            acc[char] = (acc[char] || 0) + 1
            return acc
        },{})
        const need = Object.keys(tDict).length
        let have = 0
        let current = {}

        while (r < s.length){
            current[s[r]] = (current[s[r]] || 0) + 1
            if (Object.hasOwn(tDict, s[r]) && current[s[r]] === tDict[s[r]]){
                have += 1
            }
            while (have === need){
                if (r - l + 1 < resLen){
                    resStart = l
                    resLen = r - l + 1
                }
                current[s[l]] -= 1
                if (Object.hasOwn(tDict, s[l]) && current[s[l]] < tDict[s[l]]){
                    have -= 1
                }
                l += 1
            }
            r+= 1
        }

        return resLen === s.length + 1 ? "" : s.slice(resStart, resStart + resLen)

    }
}