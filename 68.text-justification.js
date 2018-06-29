/**
 * @param {string[]} words
 * @param {number} maxWidth
 * @return {string[]}
 */
var fullJustify = function(words, maxWidth) {
    let ans = [];
    let i = 0;
    while (i < words.length) {
        let width = words[i].length;
        let line = words[i];
        let j = i + 1;
        while (j < words.length && width + words[j].length + 1 <= maxWidth) {
            width = width + words[j].length + 1;
            j++;
        }
        if (j == i + 1 || j == words.length) {
            for (let k = i + 1; k < j; k++) {
                line = line + " " + words[k];
            }
            line = line.padEnd(maxWidth);
        } else {
            let mod = (maxWidth - width) % (j - 1 - i);
            let space_count = (maxWidth - width) / (j - 1 - i) + 1;
            for (let k = i + 1; k < i + 1 + mod; k++) {
                line = line + " ".repeat(space_count + 1) + words[k];
            }
            for (let k = i + 1 + mod; k < j; k++) {
                line = line + " ".repeat(space_count) + words[k];
            }
        }
        ans.push(line);
        i = j;
    }
    return ans;
};