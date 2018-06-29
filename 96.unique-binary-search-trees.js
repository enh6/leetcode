/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    let v = new Array(n + 1).fill(0);
    v[0] = 1;
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) {
            v[i] += v[j] * v[i - j - 1];
        }
    }
    return v[n];
};