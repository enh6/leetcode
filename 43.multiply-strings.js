/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function(num1, num2) {
    let m = num1.length;
    let n = num2.length;
    let ans = new Array(m + n).fill(0);
    num1 = num1.split("").reverse();
    num2 = num2.split("").reverse();
    for(let i = 0; i < m; i++) {
        let carry = 0;
        for(let j = 0; j < n; j++) {
            let num = (ans[i + j]) + (num1[i] - '0') * (num2[j] - '0') + carry;
            ans[i + j] = num % 10;
            carry = Math.floor(num / 10);
        }
        ans[i + n] += carry;
    }
    ans.reverse();
    while (ans.length > 1 && ans[0] == 0) {
        ans.shift();
    }
    return ans.join("");
};