# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans = []
        i = 0
        while i < len(intervals):
            start = intervals[i].start
            end = intervals[i].end
            if newInterval.start > end:
                ans.append(intervals[i])
            elif newInterval.end < start:
                break
            else:
                newInterval.start = min(start, newInterval.start)
                newInterval.end = max(end, newInterval.end)
            i += 1
        ans.append(newInterval)
        ans += intervals[i:]
        return ans