/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    if (a.length < b.length) {
        return addBinary(b, a);
    }
    let c = 0;
    let sum = "";
    for (let i = a.length - 1, j = b.length - 1; i >= 0; i--, j--) {
        if (a[i] == '1') {
            c++;
        }
        if (j >= 0 && b[j] == '1') {
            c++;
        }
        sum = (c % 2 ? '1' : '0') + sum;
        c = c >> 1;
    }
    if (c) {
        return "1" + sum;
    } else {
        return sum;
    }
};