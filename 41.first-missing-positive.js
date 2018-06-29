/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        while (nums[i] - 1 >= 0 && nums[i] - 1 < nums.length && nums[nums[i] - 1] != nums[i]) {
            let tmp = nums[nums[i] - 1];
            nums[nums[i] - 1] = nums[i];
            nums[i] = tmp;
        }
    }
    let j;
    for (j = 0; j < nums.length; j++) {
        if (nums[j] - 1 != j) {
            break;
        }
    }
    return j + 1;
};