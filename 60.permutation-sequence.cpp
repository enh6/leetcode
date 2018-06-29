class Solution {
public:
    string getPermutation(int n, int k) {
        k -= 1;
        vector<bool> used(n + 1, false);
        string ans;
        int total = 1;
        for (int i = 1; i <= n; i++) {
            total = total * i;
        }
        for (int i = n; i > 0; i--) {
            total /= i;
            int j = k / total;
            k = k % total;
            for (int l = 1; l <= n; l++) {
                if (used[l]) {
                    continue;
                }
                if (j == 0) {
                    ans += ('0' + l);
                    used[l] = true;
                    break;
                }
                j--;
            }
        }
        return ans;
    }
};