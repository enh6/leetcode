/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function(intervals) {
    let ans = [];
    if (intervals.length == 0) {
        return ans;
    }
    intervals.sort((a, b) => a.start - b.start);
    let start = intervals[0].start;
    let end = intervals[0].end;
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i].start <= end) {
            end = Math.max(end, intervals[i].end);
        } else {
            ans.push(new Interval(start, end));
            start = intervals[i].start;
            end = intervals[i].end;
        }
    }
    ans.push(new Interval(start, end));
    return ans;
};