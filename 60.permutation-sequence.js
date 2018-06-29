/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    k--;
    let nums = [];
    let ans = "";
    let total = 1;
    for (let i = 1; i <= n; i++) {
        total = total * i;
        nums.push(i);
    }
    for (let i = n; i > 0; i--) {
        total /= i;
        let j = Math.floor(k / total);
        k = k % total;
        ans += nums[j];
        nums.splice(j, 1);
    }
    return ans;
};