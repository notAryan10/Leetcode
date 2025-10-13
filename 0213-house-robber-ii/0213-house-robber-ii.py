class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def func(arr):
            size = len(arr)
            memo = {}
            vis = [False] * size

            def func2(i):
                if i >= size:
                    return 0
                if vis[i]:
                    return memo[i]
                
                take = arr[i] + func2(i + 2)
                skip = func2(i + 1)
                memo[i] = max(take, skip)
                vis[i] = True
                return memo[i]
            
            return func2(0)
        
        h1 = func(nums[:-1])
        h2 = func(nums[1:])
        
        return max(h1, h2)