/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }
    let r = 0;
    while (r < x) {
        r = r * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    return r === x || Math.floor(r / 10) === x;
};