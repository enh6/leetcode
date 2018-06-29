class Solution {
public:
    void add(vector<string> &ret, string s, int n, int m) {
        if (n > m) {
            return;
        }
        if (m == 0 && n == 0) {
            ret.push_back(s);
        }
        if (n > 0) {
            add(ret, s + '(', n - 1, m);
        }
        if (m > 0) {
            add(ret, s + ')', n, m - 1);
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> ret;
        add(ret, "", n, n);
        return ret;
    }
};