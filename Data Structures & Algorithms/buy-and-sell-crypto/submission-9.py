class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        mx_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
               mx_profit = max(mx_profit, prices[right] - prices[left])
            else:
                left = right

            right +=1

        return mx_profit