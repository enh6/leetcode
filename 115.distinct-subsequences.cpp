class Solution {
public:
    int numDistinct(string s, string t) {
        if (s.empty() || t.empty() || s.length() < t.length()) {
            return 0;
        }
        vector<int> dp(t.length(), 0);
        if (s[0] == t[0]) {
            dp[0] = 1;
        }
        for (int i = 1; i < s.length(); i++) {
            for (int j = t.length() - 1; j > 0; j--) {
                if (s[i] == t[j]) {
                    dp[j] = dp[j] + dp[j-1];
                }
            }
            if (s[i] == t[0]) {
                dp[0]++;
            }
        }
        return dp[t.length() - 1];
    }
};
