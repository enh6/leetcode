/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    str = str.trim();
    if (str.length === 0) {
        return 0;
    }
    let i = 0, sign = 1, r = 0;
    if (str[0] === '+') {
        i++;
    } else if (str[0] === '-') {
        i++;
        sign = -1;
    }
    if (i === str.length) {
        return 0;
    }
    while (i < str.length && str[i] >= '0' && str[i] <= '9') {
        r = r * 10 + (str[i] - '0');
        i++;
        if (sign * r > 2147483647) {
            return 2147483647;
        } else if (sign * r < -2147483648) {
            return -2147483648;
        }
    }
    return sign * r;
};