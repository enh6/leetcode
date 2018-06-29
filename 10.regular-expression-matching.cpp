class Solution {
public:
    bool isMatch(string s, string p) {
        int i = 0, j = 0;
        while(j < p.length()) {
            if (j + 1 < p.length() && p[j + 1] == '*') {
                if (isMatch(s.substr(i), p.substr(j + 2))) {
                    return true;
                }
                int k = 0;
                while (i + k < s.length() && (s[i + k] == p[j] || p[j] == '.')) {
                    if (isMatch(s.substr(i + k + 1), p.substr(j + 2))) {
                        return true;
                    }
                    k++;
                }
                return false;
            } else if (i < s.length() && (p[j] == s[i] || p[j] == '.')) {
                    i++;
                    j++;
            } else {
                return false;
            }
        }
        return i == s.length();
    }
};