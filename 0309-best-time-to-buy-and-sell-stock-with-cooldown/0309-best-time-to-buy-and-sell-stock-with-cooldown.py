class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        
        def func(i, j):
            if i >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j:
                sell = prices[i] + func(i + 2, False)
                hold = func(i + 1, True)
                memo[(i, j)] = max(sell, hold)
            else:
                buy = -prices[i] + func(i + 1, True)
                rest = func(i + 1, False)
                memo[(i, j)] = max(buy, rest)
            
            return memo[(i, j)]
        
        return func(0, False)