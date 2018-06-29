class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s[0] == '0') {
            return 0;
        }
        int last = 1;
        int before_last = 1;
        for (int i = 1; i < s.length(); i++) {
            int cur;
            if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6' && s[i] >= '0')) {
                cur = s[i] == '0' ? before_last : last + before_last;
            } else if (s[i] == '0') {
                return 0;
            } else {
                cur = last;
            }
            before_last = last;
            last = cur;
        }
        return last;
    }
};