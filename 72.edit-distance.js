/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    let m = word1.length;
    let n = word2.length;
    let dp = [];
    for (let i = 0; i <= n; i++) {
        dp.push(i);
    }
    for (let i = 1; i <= m; i++) {
        let pre = dp[0];
        dp[0] = i;
        for (let j = 1; j <= n; j++) {
            let cur = dp[j];
            if (word1[i - 1] == word2[j - 1]) {
                dp[j] = pre;
            } else {
                dp[j] = Math.min(pre, dp[j], dp[j - 1]) + 1;
            }
            pre = cur;
        }
    }
    return dp[n];
};