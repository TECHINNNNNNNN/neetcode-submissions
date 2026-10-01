class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const tmpMap = new Map()

        for (const str of strs){
            const sortedStr = str.split('').sort().join('')

            if (!tmpMap.has(sortedStr)){
                tmpMap.set(sortedStr, [])
            }
            tmpMap.get(sortedStr).push(str)
        }

        return [...tmpMap.values()]
    }
}
