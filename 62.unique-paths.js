/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let co = new Array(m + n - 1).fill(0);
    co[0] = 1;
    for (let i = 1; i < m + n - 1; i++) {
        for (let j = i; j > 0; j--) {
            co[j] = co[j] + co[j - 1];
        }
    }
    return co[m - 1];
};