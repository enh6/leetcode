/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let nums = [1];
    while (--n) {
        let nums2 = [];
        for (let i = 0; i < nums.length; i++) {
            let j = 1;
            while (i + 1 < nums.length && nums[i] == nums[i + 1]) {
                j++;
                i++;
            }
            nums2.push(j);
            nums2.push(nums[i]);
        }
        nums = nums2;
    }
    return nums.join("");
};