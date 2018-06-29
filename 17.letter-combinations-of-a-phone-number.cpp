class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> strs;
        if (digits.empty()) {
            return strs;
        }
        string init_str = "";
        map<char, string> lut{
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"},
        };
        for (int i = 0; i < digits.length(); i++) {
            init_str +=  lut[digits[i]][0];
        }
        strs.push_back(init_str);
        for (int i = 0; i < digits.length(); i++) {
            int n = strs.size();
            for (int j = 0; j < n; j++) {
                string str = strs[j];
                string replace = lut[digits[i]];
                for (int k = 1; k < replace.length(); k++) {
                    str[i] = replace[k];
                    strs.push_back(str);
                }
            }
        }
        return strs;
    }
};