class Solution {
public:
    bool isValid(string s) {
        if (s == "0") {
            return true;
        }
        if (s[0] == '0') {
            return false;
        }
        return stoi(s) < 256;
    }

    vector<string> restoreIpAddresses(string s) {
        vector<string> ans;
        int n = s.length();
        int r[3] = {1, 2, 3};
        for (int a : r)
        for (int b : r)
        for (int c : r)
        for (int d : r)
            if (a + b + c + d == n) {
                string s1 = s.substr(0, a);
                string s2 = s.substr(a, b);
                string s3 = s.substr(a + b, c);
                string s4 = s.substr(a + b + c);
                if (isValid(s1) && isValid(s2) && isValid(s3) && isValid(s4)) {
                    ans.push_back(s1 + '.' + s2 + '.' + s3 + '.' + s4);
                }
            }
        return ans;
    }
};