/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    let max_pos = 0;
    let min_pos = 0;
    let step = 0;
    while (max_pos < nums.length - 1) {
        step++;
        let next_max_pos = max_pos + 1;
        for (let i = min_pos; i <= max_pos; i++) {
            next_max_pos = Math.max(next_max_pos, i + nums[i]);
        }
        min_pos = max_pos + 1;
        max_pos = next_max_pos;
    }
    return step;
};