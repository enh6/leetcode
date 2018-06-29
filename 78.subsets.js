/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    let ans = [[]];
    for (let i = 0; i < nums.length; i++) {
        let n = ans.length;
        for (let j = 0; j < n; j++) {
            let a = _.clone(ans[j]);
            a.push(nums[i]);
            ans.push(a);
        }
    }
    return ans;
};