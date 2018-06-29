/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let r = 0, w = 0, b = nums.length - 1;
    while (w <= b) {
        if (nums[w] == 0) {
            nums[w] = nums[r];
            nums[r] = 0;
            r++;
            w++;
        } else if (nums[w] == 2) {
            nums[w] = nums[b];
            nums[b] = 2;
            b--;
        } else {
            w++;
        }
    }
};