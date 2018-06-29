/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    let ret = [];
    if (nums.length < 4) {
        return ret;
    }
    nums.sort(function(a, b) {
        return a - b;
    });
    for (let i = 0; i < nums.length - 3; i++) {
        for (let j = i + 1; j < nums.length - 2; j++) {
            let t = target - nums[i] - nums[j];
            let k = j + 1, l = nums.length - 1;
            while (k < l) {
                if (nums[k] + nums[l] == t) {
                    ret.push([nums[i], nums[j], nums[k], nums[l]]);
                    while (k < l && nums[k + 1] == nums[k]) {
                        k++;
                    }
                    while (k < l && nums[l - 1] == nums[l]) {
                        l--;
                    }
                    k++;
                    l--;
                } else if (nums[k] + nums[l] > t) {
                    l--;
                } else {
                    k++;
                }
            }
            while (j + 1 < nums.length && nums[j + 1] == nums[j]) {
                j++;
            }
        }
        while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
            i++;
        }
    }
    return ret;
};