/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    if (s.length == 0 || s[0] == '0') {
        return 0;
    }
    let last = 1;
    let before_last = 1;
    for (let i = 1; i < s.length; i++) {
        let cur;
        if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6' && s[i] >= '0')) {
            cur = s[i] == '0' ? before_last : last + before_last;
        } else if (s[i] == '0') {
            return 0;
        } else {
            cur = last;
        }
        before_last = last;
        last = cur;
    }
    return last;
};