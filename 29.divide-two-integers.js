/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    let sign = (dividend < 0) ^ (divisor < 0);
    let ret = 0;
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    while (dividend >= divisor) {
        let n = 1;
        let div = divisor;
        while (dividend >= div + div) {
            div = div + div;
            n = n + n;
        }
        dividend -= div;
        ret += n;
    }
    if (sign) {
        ret = -ret;
    }
    if (ret < -Math.pow(2, 31) || ret > Math.pow(2, 31) - 1) {
        return Math.pow(2, 31) - 1;
    } else {
        return ret;
    }
};