/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    let ans = x;
    while (ans * ans > x) {
        ans = Math.floor((ans + x / ans) / 2);
    }
    return ans;
};