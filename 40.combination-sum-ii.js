/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
    let combination = function(candidates, target, pos, current, ans) {
        if (target == 0) {
            for (let i = 0; i < ans.length; i++) {
                if (ans[i].toString() == current.toString()) {
                    return;
                }
            }
            ans.push(current.slice());
            return;
        }
        if (target < 0) {
            return;
        }
        for (let i = pos; i < candidates.length; i++) {
            current.push(candidates[i]);
            combination(candidates, target - candidates[i], i + 1, current, ans);
            current.pop();
        }
    }
    let ans = [];
    let current = [];
    candidates.sort(function(a, b) {
        return a - b;
    })
    combination(candidates, target, 0, current, ans);
    return ans;
};