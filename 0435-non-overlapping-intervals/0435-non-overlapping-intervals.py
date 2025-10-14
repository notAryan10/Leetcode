class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1]) 
        count = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start < prev_end:
                count += 1
            else:
                prev_end = end 
        return count

        