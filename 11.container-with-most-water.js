/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let max_area = 0;
    let i = 0, j = height.length - 1;
    while (i < j) {
        max_area = Math.max(max_area, Math.min(height[i], height[j]) * (j - i));
        height[i] > height[j] ? j-- : i++;
    }
    return max_area;
};