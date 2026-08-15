class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices) - 1):
            j = i + 1
            buyPrice = prices[i]
            while j < len(prices) and prices[j] > prices[i]:
                profit = prices[j] - buyPrice
                maxProfit = max(profit, maxProfit)
                j += 1
        

        return maxProfit

        