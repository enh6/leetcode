/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let left = 0, right = nums.length - 1;
    while (left < right) {
        let mid = Math.floor((left + right) / 2);
        if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    if (nums.length == 0 || nums[left] != target) {
        return [-1, -1];
    }
    let start = left;
    right = nums.length - 1;
    while (left < right) {
        let mid = Math.floor((left + right + 1) / 2);
        if (nums[mid] <= target) {
            left = mid;
        } else {
            right = mid - 1;
        }
    }
    return [start, left];
};