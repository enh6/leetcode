class Solution {
public:
    string removeStars(string s) {
        vector<char> chars;
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (c == '*') {
                chars.pop_back();
            } else {
                chars.push_back(c);
            }
        }
        string ret(chars.begin(), chars.end());
        return ret;
    }
};
