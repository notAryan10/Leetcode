class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}

        def func(i, amount):
            if amount == 0:
                return 0
            if i == n or amount < 0:
                return 10**9

            if (i, amount) in memo:
                return memo[(i, amount)]

            pick = 1 + func(i, amount - coins[i])

            unpick = func(i + 1, amount)

            memo[(i, amount)] = min(pick, unpick)
            return memo[(i, amount)]

        ans = func(0, amount)
        if ans == 10**9:
            return -1
        else:
            return ans