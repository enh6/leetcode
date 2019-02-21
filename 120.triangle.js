/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    var sums = triangle[0];
    for (var i = 1; i < triangle.length; i++) {
        var row = triangle[i];
        var len = row.length;
        var new_sums = Array(len);
        new_sums[0] = sums[0] + row[0];
        for (var j = 1; j < len - 1; j++) {
            new_sums[j] = Math.min(sums[j - 1], sums[j]) + row[j];
        }
        new_sums[len - 1] = sums[len - 2] + row[len - 1];
        sums = new_sums;
    }
    return _.min(sums);
};
