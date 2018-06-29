/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    for (let i = 1; i < m; i++) {
        grid[i][0] = grid[i - 1][0] + grid[i][0];
    }
    for (let i = 1; i < n; i++) {
        grid[0][i] = grid[0][i - 1] + grid[0][i];
    }
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            grid[i][j] = Math.min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j];
        }
    }
    return grid[m - 1][n - 1];
};