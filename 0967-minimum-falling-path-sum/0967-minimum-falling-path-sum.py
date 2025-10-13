class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        memo = {}

        def func(i, j):
            if j < 0 or j >= m:
                return float('inf')
            if i == n - 1:
                return matrix[i][j]
            if (i, j) in memo:
                return memo[(i, j)]
            
            down = func(i + 1, j)
            diag_left = func(i + 1, j - 1)
            diag_right = func(i + 1, j + 1)
            memo[(i, j)] = matrix[i][j] + min(down, diag_left, diag_right)
            return memo[(i, j)]
        ans = float('inf')
        for k in range(m):
            ans = min(ans, func(0, k))
        return ans        