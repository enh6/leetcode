/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows == 1) {
        return s;
    }
    let z = "";
    for (let i = 0; i < numRows; i++) {
        for (let j = i; j < s.length; j += 2 * numRows - 2) {
            z += s[j];
            if (i != 0 && i != numRows - 1 && j + 2 * (numRows - i - 1) < s.length) {
                z += s[j + 2 * (numRows - i - 1)];
            }
        }
    }
    return z;
};