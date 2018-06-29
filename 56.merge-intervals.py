# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        if not intervals:
            return ans
        intervals.sort(key = lambda i: i.start)
        start = intervals[0].start
        end = intervals[0].end
        for i in intervals:
            if i.start <= end:
                end = max(end, i.end)
            else:
                ans.append(Interval(start, end))
                start = i.start
                end = i.end
        ans.append(Interval(start, end))
        return ans