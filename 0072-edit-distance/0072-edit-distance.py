class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        memo = {}

        def func(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            if (i, j) in memo:
                return memo[(i, j)]
            
            if word1[i] == word2[j]:
                memo[(i, j)] = func(i + 1, j + 1)
            else: 
                insert = 1 + func(i, j + 1)
                delete = 1 + func(i + 1, j)
                replace = 1 + func(i + 1, j + 1)
                memo[(i , j)] = min(insert, delete, replace)
            return memo[(i, j)]
        return func(0, 0)