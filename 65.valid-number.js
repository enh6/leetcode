/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    // \s* space
    // \d+(\.\d*)?|\.\d+ float
    // [+-]?\\d+ integer
    let regex = /^\s*[+-]?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?\s*$/;
    return regex.test(s);
};