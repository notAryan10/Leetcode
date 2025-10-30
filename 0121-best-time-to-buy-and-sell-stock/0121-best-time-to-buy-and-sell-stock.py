class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        mini = prices[0]
        max_profit = 0

        for i in range(1, n):
            profit = prices[i] - mini
            if profit > max_profit:
                max_profit = profit
            if prices[i] < mini:
                mini = prices[i]
        return max_profit