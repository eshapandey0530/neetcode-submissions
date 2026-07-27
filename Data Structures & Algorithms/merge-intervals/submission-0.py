class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        n = len(intervals)
        intervals.sort()
        merged = [intervals[0]]

        for i in range(1, n):

            start_time = intervals[i][0]
            end_time = intervals[i][1]

            last_end = merged[-1][1]

            if start_time <= last_end:
                merged[-1][1] = max(end_time, last_end)

            else:
                merged.append(intervals[i])

        return merged
