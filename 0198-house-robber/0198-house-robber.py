class Solution:
    def rob(self, nums: List[int]) -> int:
        def maxSum(n,nums):
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            
            dp2 = nums[0]
            dp1 = max(nums[0], nums[1])

            for i in range(2, n):
                curr = max(dp1, nums[i] + dp2)
                dp2, dp1 = dp1, curr
            return dp1
        return maxSum(len(nums), nums)