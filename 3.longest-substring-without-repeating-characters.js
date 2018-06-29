/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let max_length = 0, begin = -1;
    let map = {};
    for (let end = 0; end < s.length; end++) {
        if (_.has(map, s[end]) && map[s[end]] > begin) {
            begin = map[s[end]];
        }
        map[s[end]] = end;
        max_length = Math.max(max_length, end - begin);
    }
    return max_length;
};