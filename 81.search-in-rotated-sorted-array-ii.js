/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var search = function(nums, target) {
    if (nums.length == 0) {
        return false;
    }
    let left = 0, right = nums.length - 1;
    while (nums[left] == nums[right] && left != right) {
        right--;
    }
    while (left <= right) {
        let mid = (left + right) >> 1;
        if (nums[mid] == target) {
            return true;
        } else if (nums[mid] >= nums[left]) {
            if (target >= nums[left] && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }
    return false;
};