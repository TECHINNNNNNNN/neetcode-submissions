class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const tmpMap = new Map()

        for (const str of strs){
            const keyArray = Array(26).fill(0)
            for (const c of str){
                const index = c.codePointAt(0) - 'a'.codePointAt(0)
                keyArray[index] += 1
            }

            const strKey = keyArray.join(',')
            if (!tmpMap.has(strKey)){
                tmpMap.set(strKey, [])
            }
            tmpMap.get(strKey).push(str)

        }

        return [...tmpMap.values()]
    }
}
