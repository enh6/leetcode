/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {
    let ret = [];
    let wl = words[0].length;
    let wc = words.length;
    if (s.length < wl * wc) {
        return ret;
    }
    let occurs = {};
    let count = 0;
    for (let i = 0; i < wc; i++) {
        if (occurs[words[i]]) {
            occurs[words[i]]++;
        } else {
            occurs[words[i]] = 1;
            count++;
        }
    }
    for (let i = 0; i <= s.length - wl * wc; i++) {
        let occ = {};
        let cnt = 0;
        for (let j = 0; j < wc; j++) {
            let w = s.substr(i + j * wl, wl);
            if (!occurs[w]) {
                break;
            } else {
                occ[w] ? occ[w]++ : occ[w] = 1;
                if (occ[w] == occurs[w]) {
                    cnt++;
                } else if (occ[w] > occurs[w]) {
                    break;
                }
            }
        }
        if (cnt == count) {
            ret.push(i);
        }
    }
    return ret;
};