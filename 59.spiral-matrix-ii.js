/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    let ans = [];
    for (let i = 0; i < n; i++) {
        ans.push(new Array(n));
    }
    let num = 1;
    for (let i = 0; i < (n - 1) / 2; i++) {
        for (let j = i; j < n - i; j++) {
            ans[i][j] = num++;
        }
        for (let j = i + 1; j < n - 1 - i; j++) {
            ans[j][n - 1 - i] = num++;
        }
        for (let j = n - 1 - i; j >= i; j--) {
            ans[n - 1 - i][j] = num++;
        }
        for (let j = n - 1 - i - 1; j > i; j--) {
            ans[j][i] = num++;
        }
    }
    if (n % 2) {
        ans[Math.floor(n / 2)][Math.floor(n / 2)] = num;
    }
    return ans;
};