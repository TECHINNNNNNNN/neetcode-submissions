class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = []
        const bracket = {")":"(", "]":"[","}":"{"}

        for (const b of s){
            if (Object.hasOwn(bracket, b)){
                if (stack.length !== 0 && stack[stack.length - 1] === bracket[b]){
                    stack.pop()
                }
                else {
                    return false
                }
            } else {
                stack.push(b)
            }
        }

        return stack.length === 0 ? true : false
    }
}