class Solution {
public:
    bool isScramble(string s1, string s2) {
        string s1_sorted = s1;
        sort(s1_sorted.begin(), s1_sorted.end());
        string s2_sorted = s2;
        sort(s2_sorted.begin(), s2_sorted.end());
        if (s1_sorted != s2_sorted) {
            return false;
        }
        int len = s1.length();
        if (len <= 3) {
            return true;
        }
        for (int i = 1; i < len; i++) {
            if (isScramble(s1.substr(0, i), s2.substr(0, i)) &&
                isScramble(s1.substr(i, len - i), s2.substr(i, len - i))) {
                return true;
            }
            if (isScramble(s1.substr(0, i), s2.substr(len - i, i)) &&
                isScramble(s1.substr(i, len - i), s2.substr(0, len - i))) {
                return true;
            }
        }
        return false;
    }
};