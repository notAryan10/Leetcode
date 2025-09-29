class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def func(i , j):
            if i == 1 and j == 1:
                return 1
            if i < 1 or j < 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = func(i - 1, j) + func(i , j - 1)
            return memo[(i, j)]
        return func(n ,m)