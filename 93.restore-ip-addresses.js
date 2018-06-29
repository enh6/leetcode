/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    let ans = [];
    let n = s.length;
    let isValid = function(s) {
        if (s == "0") {
            return true;
        }
        if (s[0] == '0') {
            return false;
        }
        return +s < 256;
    };
    for (let a = 1; a <= 3; a++)
    for (let b = 1; b <= 3; b++)
    for (let c = 1; c <= 3; c++)
    for (let d = 1; d <= 3; d++)
        if (a + b + c + d == n) {
            let s1 = s.substr(0, a);
            let s2 = s.substr(a, b);
            let s3 = s.substr(a + b, c);
            let s4 = s.substr(a + b + c);
            if (isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)) {
                ans.push(s1 + '.' + s2 + '.' + s3 + '.' + s4);
            }
        }
    return ans;
};