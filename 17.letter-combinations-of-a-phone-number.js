/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    let strs = [];
    if (!digits) {
        return strs;
    }
    let lut = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    };
    let init_str = "";
    for (let i = 0; i < digits.length; i++) {
        init_str +=  lut[digits[i]][0];
    }
    strs.push(init_str);
    for (let i = 0; i < digits.length; i++) {
        let n = strs.length;
        for (let j = 0; j < n; j++) {
            let replace = lut[digits[i]];
            for (let k = 1; k < replace.length; k++) {
                let str = strs[j];
                strs.push(str.substr(0, i) + replace[k] + str.substr(i + 1));
            }
        }
    }
    return strs;
};