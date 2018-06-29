/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @param {Interval} newInterval
 * @return {Interval[]}
 */
var insert = function(intervals, newInterval) {
    let ans = [];
    let i;
    for (i = 0; i < intervals.length; i++) {
        let start = intervals[i].start;
        let end = intervals[i].end;
        if (newInterval.start > end) {
            ans.push(intervals[i]);
        } else if (newInterval.end < start) {
            break;
        } else {
            newInterval.start = Math.min(start, newInterval.start);
            newInterval.end = Math.max(end, newInterval.end);
        }
    }
    ans.push(newInterval);
    for (let j = i; j < intervals.length; j++) {
        ans.push(intervals[j]);
    }
    return ans;
};