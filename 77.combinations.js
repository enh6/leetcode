/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    if (k == 0) {
        return [[]];
    }
    if (k == n) {
        let a = [];
        for (let i = 1; i <= n; i++) {
            a.push(i);
        }
        return [a];
    }
    let ans1 = combine(n - 1, k);
    let ans2 = combine(n - 1, k - 1);
    for (let i = 0; i < ans2.length; i++) {
        ans2[i].push(n);
        ans1.push(ans2[i]);
    }
    return ans1;
};