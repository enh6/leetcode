/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    if (matrix.length == 0 || matrix[0].length == 0) {
        return false;
    }
    let n = matrix[0].length;
    let i = 0, j = matrix.length - 1;
    while (i <= j) {
        let mid = (i + j) >> 1;
        if (matrix[mid][0] > target) {
            j = mid - 1;
        } else if (matrix[mid][n - 1] < target) {
            i = mid + 1;
        } else {
            i = 0, j = n - 1;
            while (i <= j) {
                let mid2 = (i + j) >> 1;
                if (matrix[mid][mid2] > target) {
                    j = mid2 - 1;
                } else if (matrix[mid][mid2] < target) {
                    i = mid2 + 1;
                } else {
                    return true;
                }
            }
        }
    }
    return false;
};