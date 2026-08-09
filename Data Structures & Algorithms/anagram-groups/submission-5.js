class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const outputDict = new Map();
        const aCode = 'a'.charCodeAt(0);

        for (const word of strs) {
            const count = new Array(26).fill(0);

            for (const char of word) {
                count[char.charCodeAt(0) - aCode] += 1;
            }

            const key = count.join(',');

            if (!outputDict.has(key)) {
                outputDict.set(key, []);
            }
            outputDict.get(key).push(word);
        }

        return [...outputDict.values()];
    }
}