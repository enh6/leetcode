/**
 * @param {number} n
 * @return {string[]}
 */
var add = function(ret, s, n, m) {
    if (n > m) {
        return;
    }
    if (m == 0 && n == 0) {
        ret.push(s);
    }
    if (n > 0) {
        add(ret, s + '(', n - 1, m);
    }
    if (m > 0) {
        add(ret, s + ')', n, m - 1);
    }
};

var generateParenthesis = function(n) {
    let ret = [];
    add(ret, "", n, n);
    return ret;
};