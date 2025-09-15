class Solution:
    def tribonacci(self, n: int) -> int:
        def func(n, m={}):
            if n <= 1:
                return n
            if n == 2:
                return 1
            if n in m:
                return m[n]
            m[n] = func(n - 1, m) + func(n - 2, m) + func(n - 3, m)
            return m[n]
        return func(n, {})
