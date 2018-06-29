/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    for (let i = nums.length - 1; i > 0; i--) {
        if (nums[i - 1] < nums[i]) {
            for (let j = nums.length - 1; j >= i; j--) {
                if (nums[j] > nums[i - 1]) {
                    let tmp = nums[i - 1];
                    nums[i - 1] = nums[j];
                    nums[j] = tmp;
                    for (let j = i, k = nums.length - 1; j < k; j++, k--) {
                        let tmp = nums[j];
                        nums[j] = nums[k];
                        nums[k] = tmp;
                    }
                    return;
                }
            }
        }
    }
    nums.reverse();
    return;
};

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    let ans = [];
    ans.push(nums.slice());
    nextPermutation(nums);
    while (!_.isEqual(nums, ans[0])) {
        ans.push(nums.slice());
        nextPermutation(nums);
    }
    return ans;
};