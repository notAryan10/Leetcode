class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        memo = {}

        def func(i, j):
            if i >= n or j >= m:
                return float("inf")
            if i == n - 1 and j == m - 1:
                return max(1, 1 - dungeon[i][j])
            if (i, j) in memo:
                return memo[(i, j)]
            
            down = func(i + 1, j)
            right = func(i, j + 1)
            need = min(down, right) - dungeon[i][j]
            memo[(i, j)] = max(1, need)
            return memo[(i, j)]
        return func(0, 0)