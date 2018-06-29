class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n));
        int num = 1;
        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - i; j++) {
                ans[i][j] = num++;
            }
            for (int j = i + 1; j < n - 1 - i; j++) {
                ans[j][n - 1 - i] = num++;
            }
            for (int j = n - 1 - i; j >= i; j--) {
                ans[n - 1 - i][j] = num++;
            }
            for (int j = n - 1 - i - 1; j > i; j--) {
                ans[j][i] = num++;
            }
        }
        if (n % 2) {
            ans[n / 2][n / 2] = num;
        }
        return ans;
    }
};