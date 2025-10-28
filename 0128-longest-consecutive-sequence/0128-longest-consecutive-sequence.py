class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums.sort()
        ans = 1
        streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                streak += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                ans = max(ans, streak)
                streak = 1

        ans = max(ans, streak)  
        return ans
