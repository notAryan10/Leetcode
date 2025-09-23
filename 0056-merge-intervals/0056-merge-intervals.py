class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def merge(intervals):
            intervals.sort()
            merged = []
            prev_start, prev_end = intervals[0]
            
            for i in range(1, len(intervals)):
                start, end = intervals[i]
                if start <= prev_end:  
                    prev_end = max(prev_end, end)  
                else:
                    merged.append([prev_start, prev_end])
                    prev_start, prev_end = start, end
            
            merged.append([prev_start, prev_end])
            return merged
        return merge(intervals)