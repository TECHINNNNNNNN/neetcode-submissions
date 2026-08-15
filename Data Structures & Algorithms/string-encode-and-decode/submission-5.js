class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded = ''
        for (const word of strs){
            const wordLength = word.length
            encoded += wordLength 
            encoded += '@'
            encoded += word
        }

        console.log(encoded)

        return encoded
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let decoded = []

        let i = 0

        while (i < str.length){
            let j = i
            while (str[j] != '@') {
                j += 1
            }
            const lenghtOfWord = parseInt(str.slice(i, j))
            const actualWord = str.slice(j + 1, j + 1 + lenghtOfWord)
            decoded.push(actualWord)
            i = j + 1 + lenghtOfWord
        }

        return decoded
    }
}
