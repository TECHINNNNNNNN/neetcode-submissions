class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def helper(remaining):
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return -1
            

            if remaining in cache:
                return cache[remaining]
            
            minCoins = float('inf')
            for coin in coins:
                result = helper(remaining - coin)
                if result != -1:
                    minCoins = min(minCoins, 1 + result)
            
            cache[remaining] = minCoins if minCoins != float('inf') else -1
            return cache[remaining]
        
        return helper(amount)
            
        