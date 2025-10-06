class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def func(A, i):
            if i in memo:
                return memo[i]
            
            ans = 1 
            for j in range(i):
                if A[j] < A[i]:
                    ans = max(ans, 1 + func(A, j))
            
            memo[i] = ans
            return ans

        def lenofSeq(A):
            ans = 1
            for i in range(len(A)):
                ans = max(ans, func(A, i))
            return ans

        return lenofSeq(nums)