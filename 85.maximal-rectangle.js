/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let ans = 0;
    let index = [];
    for (let i = 0; i <= heights.length; i++) {
        while (index.length != 0 && (heights[index[index.length - 1]] > heights[i] || i == heights.length)) {
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

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    if (matrix.length == 0) {
        return 0;
    }
    let ans = 0;
    let heights = new Array(matrix[0].length).fill(0);
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] == '1') {
                heights[j]++;
            } else {
                heights[j] = 0;
            }
        }
        ans = Math.max(ans, largestRectangleArea(heights));
    }
    return ans;
};