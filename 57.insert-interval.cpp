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
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval> ans;
        auto it = intervals.begin();
        for (; it < intervals.end(); it++) {
            int start = it->start;
            int end = it->end;
            if (newInterval.start > end) {
                ans.push_back(*it);
            } else if (newInterval.end < start) {
                break;
            } else {
                newInterval.start = min(start, newInterval.start);
                newInterval.end = max(end, newInterval.end);
            }
        }
        ans.push_back(newInterval);
        ans.insert(ans.end(), it, intervals.end());
        return ans;
    }
};