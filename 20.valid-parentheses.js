/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stk = []
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(' || s[i] === '{' || s[i] === '[') {
            stk.push(s[i]);
        } else if (s[i] === ')') {
            if (stk.length === 0 || stk.pop() !== '(') {
                return false;
            }
        } else if (s[i] === ']') {
            if (stk.length === 0 || stk.pop() !== '[') {
                return false;
            }
        } else if (s[i] === '}') {
            if (stk.length === 0 || stk.pop() !== '{') {
                return false;
            }
        }
    }
    return stk.length === 0;
};