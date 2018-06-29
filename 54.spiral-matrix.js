/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let ans = [];
    let m = matrix.length;
    if (m == 0) {
        return ans;
    }
    let n = matrix[0].length;
    for (let i = 0; i < m / 2 && i < n / 2; i++) {
        if (i == m - 1 - i) {
            for(let j = i; j < n - i; j++) {
                ans.push(matrix[i][j]);
            }
            break;
        }
        if (i == n - 1 - i) {
            for (let j = i; j <= m - 1 - i; j++) {
                ans.push(matrix[j][i]);
            }
            break;
        }
        for (let j = i; j < n - i; j++) {
            ans.push(matrix[i][j]);
        }
        for (let j = i + 1; j < m - 1 - i; j++) {
            ans.push(matrix[j][n - 1 - i]);
        }
        for (let j = n - 1 - i; j >= i; j--) {
            ans.push(matrix[m - 1 - i][j]);
        }
        for (let j = m - 1 - i - 1; j > i; j--) {
            ans.push(matrix[j][i]);
        }
    }
    return ans;
};