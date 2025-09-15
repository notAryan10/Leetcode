class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]

            dp2 = arr[0]
            dp1 = max(arr[0], arr[1])

            for i in range(2, n):
                curr = max(dp1, arr[i] + dp2)
                dp2, dp1 = dp1, curr

            return dp1

        n = len(nums)
        if n == 1:
            return nums[0]

        case1 = func(nums[:-1])
        case2 = func(nums[1:])

        return max(case1, case2)