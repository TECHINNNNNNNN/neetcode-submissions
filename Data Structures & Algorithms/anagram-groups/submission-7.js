class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let tmpDict = {}
        for (const word of strs){
            const wordKey = word.split('').sort().join('')
            if (!tmpDict[wordKey]){
                tmpDict[wordKey] = [];
            }

            tmpDict[wordKey].push(word)
        }

        return Object.values(tmpDict)

        
    }
}
