/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return x;
    }
    if (n == -1) {
        return 1 / x;
    }
    return myPow(x, n % 2) * myPow(x * x, n > 0 ? Math.floor(n / 2) : Math.ceil(n / 2));
};