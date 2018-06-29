class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        if (k == 0) {
            return {{}};
        }
        if (k == n) {
            vector<int> a;
            for (int i = 1; i <= n; i++) {
                a.push_back(i);
            }
            return {a};
        }
        auto ans1 = combine(n - 1, k);
        auto ans2 = combine(n - 1, k - 1);
        for (auto& a : ans2) {
            a.push_back(n);
        }
        ans1.insert(ans1.end(), ans2.begin(), ans2.end());
        return ans1;
    }
};