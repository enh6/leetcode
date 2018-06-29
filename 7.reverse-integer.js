/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let sign = 1;
    if (x < 0) {
        x = -x;
        sign = -1;
    }
    let r = 0;
    while(x) {
        r = r * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    r = sign * r;
    return (r < -2147483648 || r > 2147483647) ? 0 : r;
};