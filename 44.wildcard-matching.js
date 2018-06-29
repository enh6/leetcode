/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    let i = 0, j = 0;
    let m = s.length, n = p.length;
    let match_pos = -1, pattern_pos = -1;
    while (i < m) {
        if (j < n && (s[i] == p[j] || p[j] == '?')) {
            i++; j++;
        } else if (j < n && p[j] == '*') {
            j++;
            pattern_pos = j;
            match_pos = i;
        } else if (pattern_pos != -1) {
            j = pattern_pos;
            match_pos++;
            i = match_pos;
        } else {
            return false;
        }
    }
    while (j < n && p[j] == '*') {
        j++;
    }
    return j == n;
};