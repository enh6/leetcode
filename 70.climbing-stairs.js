/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let cur = 1, last = 1;
    while (--n) {
        let tmp = cur + last;
        last = cur;
        cur = tmp;
    }
    return cur;
};