class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [0] * (amount + 1)
        memo[0] = 1   
        for i in coins:                
            for j in range(i, amount + 1):  
                memo[j] += memo[j - i]
        
        return memo[amount]