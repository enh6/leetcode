/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let max_pos = 0;
    for (let i = 0; i < nums.length && i <= max_pos; i++) {
        max_pos = Math.max(max_pos, i + nums[i]);
    }
    return max_pos >= nums.length - 1;
};