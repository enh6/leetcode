/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    let ret = [];
    if (nums.length < 3) {
        return ret;
    }
    nums.sort(function(a, b) {
        return a - b;
    });
    for (let i = 0; i < nums.length - 2; i++) {
        let target = -nums[i];
        let j = i + 1, k = nums.length - 1;
        while (j < k) {
            if (nums[j] + nums[k] == target) {
                ret.push([nums[i], nums[j], nums[k]]);
                while (j < k && nums[j + 1] == nums[j]) {
                    j++;
                }
                while (j < k && nums[k - 1] == nums[k]) {
                    k--;
                }
                j++;
                k--;
            } else if (nums[j] + nums[k] > target) {
                k--;
            } else {
                j++;
            }
        }
        while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
            i++;
        }
    }
    return ret;
};