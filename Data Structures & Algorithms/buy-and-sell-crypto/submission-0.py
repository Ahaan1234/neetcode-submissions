class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, n = 0, 1, len(prices)
        max_profit = 0
        for r in range(n):
            if prices[l] > prices[r]:
                l = r
            
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)

            r += 1
        
        return max_profit