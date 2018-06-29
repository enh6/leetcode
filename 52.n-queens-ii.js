/**
 * @param {number} n
 * @return {number}
 */
var totalNQueens = function(n) {
    let ans = 0;
    let pos = new Array(n);
    var valid = function(cur, i) {
        for (let j = 0; j < cur; j++) {
            if (pos[j] == i || pos[j] - i == j - cur || pos[j] - i == cur - j) {
                return false;
            }
        }
        return true;
    };
    var dfs = function(cur) {
        let n = pos.length;
        for (let i = 0; i < n; i++) {
            if (!valid(cur, i)) {
                continue;
            }
            pos[cur] = i;
            if (cur < n - 1) {
                dfs(cur + 1);
            } else {
                ans++;
            }
        }
    };
    dfs(0);
    return ans;
};