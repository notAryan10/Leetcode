class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def func(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            take = nums[i] + func(i + 2)
            skip = func(i + 1)
            memo[i] = max(take, skip)
            return memo[i]
        return func(0) 