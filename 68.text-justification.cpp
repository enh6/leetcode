class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ans;
        int i = 0;
        while (i < words.size()) {
            int width = words[i].length();
            string line = words[i];
            int j = i + 1;
            while (j < words.size() && width + words[j].length() + 1 <= maxWidth) {
                width = width + words[j].length() + 1;
                j++;
            }
            if (j == i + 1 || j == words.size()) {
                for (int k = i + 1; k < j; k++) {
                    line = line + " " + words[k];
                }
                line += string(maxWidth - line.length(), ' ');
            } else {
                int mod = (maxWidth - width) % (j - 1 - i);
                int space_count = (maxWidth - width) / (j - 1 - i) + 1;
                for (int k = i + 1; k < i + 1 + mod; k++) {
                    line = line + string(space_count + 1, ' ') + words[k];
                }
                for (int k = i + 1 + mod; k < j; k++) {
                    line = line + string(space_count, ' ') + words[k];
                }
            }
            ans.push_back(line);
            i = j;
        }
        return ans;
    }
};