/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    let ans = [];
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
                let vs = [];
                for (let j = 0; j < n; j++) {
                    vs.push(".".repeat(pos[j]) + 'Q' + ".".repeat(n - 1 - pos[j]));
                }
                ans.push(vs);
            }
        }
    };
    dfs(0);
    return ans;
};