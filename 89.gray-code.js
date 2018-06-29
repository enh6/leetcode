/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    if (n == 0) {
        return [0];
    }
    ans = grayCode(n - 1);
    let s = ans.length;
    for (let i = s - 1; i >= 0; i--) {
        ans.push(s + ans[i]);
    }
    return ans;
};