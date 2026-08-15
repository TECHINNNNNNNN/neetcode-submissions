class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0

        for (let i = 0; i < prices.length - 1; i ++){
            let j = i + 1
            const buyPrice = prices[i]
            while (j < prices.length && prices[j] > buyPrice){
                const profit = prices[j] - buyPrice
                maxProfit = Math.max(maxProfit, profit)
                j += 1
            }
        }

        return maxProfit
    }
}
