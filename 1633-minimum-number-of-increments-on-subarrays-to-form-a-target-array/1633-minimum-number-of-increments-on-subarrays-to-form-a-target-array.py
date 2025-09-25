class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        ans = target[0]
        prev = target[0]
        
        for i in range(1, n):
            if prev < target[i]:
                ans += target[i] - prev
            prev = target[i]
        return ans


