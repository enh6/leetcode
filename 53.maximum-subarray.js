/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let ans = nums[0];
    let sum = nums[0];
    for (let i = 1; i < nums.length; i++) {
        sum = Math.max(sum, 0);
        sum += nums[i];
        ans = Math.max(ans, sum);
    }
    return ans;
};