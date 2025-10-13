class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        memo = {}
        def func(i, j):
            if i == n - 1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i, j)]
            
            down = func(i + 1, j)
            diag_right = func(i + 1, j + 1)
            memo[(i, j)] =  triangle[i][j] + min(down, diag_right)
            return memo[(i, j)]
        return func(0, 0)