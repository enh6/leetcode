/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let combination = function(candidates, target, pos, current, ans) {
        if (target == 0) {
            ans.push(current.slice());
            return;
        }
        if (target < 0) {
            return;
        }
        for (let i = pos; i < candidates.length; i++) {
            current.push(candidates[i]);
            combination(candidates, target - candidates[i], i, current, ans);
            current.pop();
        }
    }
    let ans = [];
    let current = [];
    combination(candidates, target, 0, current, ans);
    return ans;
};