class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0
        let l = 0
        let r = 1

        while (r < prices.length){
            if (prices[l] > prices[r]){
                l = r
                r += 1
            }else if (prices[l] < prices[r]){
                maxProfit = Math.max(maxProfit, prices[r] - prices[l])
                r += 1
            } else {
                l = r
                r += 1
            }
            
        }

        return maxProfit
    }
}
