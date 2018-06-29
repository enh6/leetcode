/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    nums.sort();
    let ans = [[]];
    for (let i = 0; i < nums.length; i++) {
        let n = ans.length;
        for (let j = 0; j < n; j++) {
            let a = _.clone(ans[j]);
            a.push(nums[i]);
            ans.push(a);
        }
        let k = 1;
        while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
            for (let j = 0; j < n; j++) {
                let a = _.clone(ans[k * n + j]);
                a.push(nums[i]);
                ans.push(a);
            }
            k++;
            i++;
        }
    }
    return ans;
};