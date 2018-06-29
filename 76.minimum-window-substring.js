/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    let map = new Array(128).fill(0);
    for (let i = 0; i < t.length; i++) {
        map[t.charCodeAt(i)]++;
    }
    let begin = 0, end = 0, count = 0;
    let window_head = 0, window_length = s.length + 1;
    while (end < s.length) {
        map[s.charCodeAt(end)]--;
        if (map[s.charCodeAt(end)] >= 0) {
            count++;
        }
        if (count == t.length) {
            while (map[s.charCodeAt(begin)] < 0) {
                map[s.charCodeAt(begin)]++;
                begin++;
            }
            if (end - begin + 1 < window_length) {
                window_length = end - begin + 1;
                window_head = begin;
            }
            map[s.charCodeAt(begin)]++;
            begin++;
            count--;
        }
        end++;
    }
    return window_length > s.length ? "" : s.substr(window_head, window_length);
};