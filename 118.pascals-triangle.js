/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    var ans = [];
    var row = [];
    for (var i = 0; i < numRows; i++) {
        row.push(1);
        for (var j = row.length - 2; j > 0; j--) {
            row[j] = row[j - 1] + row[j];
        }
        ans.push(row.slice());
    }
    return ans;
};
