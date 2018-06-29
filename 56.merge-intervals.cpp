/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        vector<Interval> ans;
        if (intervals.empty()) {
            return ans;
        }
        sort(intervals.begin(), intervals.end(), [](Interval a, Interval b) {
            return a.start < b.start;
        });
        int start = intervals[0].start;
        int end = intervals[0].end;
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i].start <= end) {
                end = max(end, intervals[i].end);
            } else {
                ans.emplace_back(start, end);
                start = intervals[i].start;
                end = intervals[i].end;
            }
        }
        ans.emplace_back(start, end);
        return ans;
    }
};