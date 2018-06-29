class Solution {
public:
    vector<int> grayCode(int n) {
        if (n == 0) {
            return {0};
        }
        auto ans = grayCode(n - 1);
        int s = ans.size();
        for (int i = s - 1; i >= 0; i--) {
            ans.push_back(s + ans[i]);
        }
        return ans;
    }
};