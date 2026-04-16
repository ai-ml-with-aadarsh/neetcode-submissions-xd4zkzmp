class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        len_prices = len(prices)
        if max(prices) < 1 or len_prices < 1:
            return max_profit


        for i in range(len_prices -1):
            for j in range(i+1, len_prices):
                max_profit = max(max_profit, prices[j]-prices[i])
        
        return max_profit
