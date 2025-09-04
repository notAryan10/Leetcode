class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left = divide(nums[:mid])
            right = divide(nums[mid:])
            return merge(left, right)
        def merge(l, r):
            res = []
            i, j = 0, 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    res.append(l[i])
                    i += 1
                else: 
                    res.append(r[j])
                    j += 1
            res.extend(l[i:])
            res.extend(r[j:])
            return res
        return divide(nums)

            