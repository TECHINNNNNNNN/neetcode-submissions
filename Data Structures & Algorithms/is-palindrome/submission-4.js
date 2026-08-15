class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0;
        let r = s.length - 1;


        while (l < r){
            if (!this.isAlphanumeric(s[l])){
                l += 1
            } else if (!this.isAlphanumeric(s[r])){
                r -= 1
            } else {
                if (s[l].toLowerCase() != s[r].toLowerCase()){
                    return false
                }
                l += 1
                r -= 1
            }
        }

        return true
    }

    isAlphanumeric(str) {
        return /^[a-z0-9]+$/i.test(str);
    }
}
