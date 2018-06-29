/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} s3
 * @return {boolean}
 */
var isInterleave = function(s1, s2, s3) {
    let m = s1.length;
    let n = s2.length;
    if (m + n != s3.length) {
        return false;
    }
    let dp = [];
    for (let i = 0; i <= m; i++) {
        dp.push(new Array(n + 1).fill(false));
    }
    dp[0][0] = true;
    for (let i = 1; i <= m; i++) {
        dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
    }
    for (let i = 1; i <= n; i++) {
        dp[0][i] = dp[0][i - 1] && s2[i - 1] == s3[i - 1];
    }
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            dp[i][j] = (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1])
                || (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]);
        }
    }
    return dp[m][n];
};