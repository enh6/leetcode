/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let pos = 0, n = 1;
    for (let i = 0; i < s.length; i++) {
        let left = i - 1, right = i + 1;
        while (right < s.length && s[i] == s[right]) {
            right++;
        }
        while (left >= 0 && right < s.length && s[left] == s[right]) {
            left--;
            right++;
        }
        if (right - left - 1 > n) {
            pos = left + 1;
            n = right - left - 1;
        }
    }
    return s.substr(pos, n);
};