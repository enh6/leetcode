/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let ans = 0;
    let index = [];
    for (let i = 0; i <= heights.length; i++) {
        while (index.length != 0 && (i == heights.length || heights[index[index.length - 1]] > heights[i])) {
            let h = heights[index.pop()];
            if (index.length == 0) {
                ans = Math.max(ans, h * i);
            } else {
                ans = Math.max(ans, h * (i - index[index.length - 1] - 1));
            }
        }
        index.push(i);
    }
    return ans;
};