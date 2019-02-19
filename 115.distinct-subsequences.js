/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var numDistinct = function(s, t) {
    if (s.length < t.length) {
        return 0;
    }
    var dp = new Array(t.length).fill(0);
    if (s[0] === t[0]) {
        dp[0] = 1;
    }
    for (let i = 1; i < s.length; i++) {
        for (let j = t.length - 1; j > 0; j--) {
            if (s[i] === t[j]) {
                dp[j] = dp[j] + dp[j-1];
            }
        }
        if (s[i] === t[0]) {
            dp[0]++;
        }
    }
    return dp[t.length -1];
};
