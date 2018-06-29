/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let groups = {};
    for (let i = 0; i < strs.length; i++) {
        let str = strs[i];
        let key = str.split("").sort().join("");
        if (groups[key]) {
            groups[key].push(str);
        } else {
            groups[key] = [str];
        }
    }
    let ans = [];
    for (let key in groups) {
        ans.push(groups[key]);
    }
    return ans;
};