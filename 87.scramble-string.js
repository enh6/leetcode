/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var isScramble = function(s1, s2) {
    if (s1.split("").sort().join("") != s2.split("").sort().join("")) {
        return false;
    }
    let len = s1.length;
    if (len <= 3) {
        return true;
    }
    for (let i = 1; i < len; i++) {
        if (isScramble(s1.substr(0, i), s2.substr(0, i)) &&
            isScramble(s1.substr(i, len - i), s2.substr(i, len - i))) {
            return true;
        }
        if (isScramble(s1.substr(0, i), s2.substr(len - i, i)) &&
            isScramble(s1.substr(i, len - i), s2.substr(0, len - i))) {
            return true;
        }
    }
    return false;
};