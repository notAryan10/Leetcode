class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = {}

        def func(i, j):
            if i >= n or j >= m:
                return (10 ** 9) + 7
            if i == n - 1 and j == m - 1:
                return grid[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            
            a = func(i, j + 1)
            b = func(i + 1, j)
            memo[(i, j)] = grid[i][j] + min(a, b)
            return memo[(i, j)]

        return func(0, 0)