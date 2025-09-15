class Solution:
    def fib(self, n: int) -> int:
        def func(n , m={}):
            if n in m:
                return m[n]
            if n <= 1:
                return n
            m[n] = func(n - 1, m) + func(n - 2, m)
            return m[n]
        return func(n, {})