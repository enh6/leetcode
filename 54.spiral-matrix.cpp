class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int m = matrix.size();
        if (m == 0) {
            return ans;
        }
        int n = matrix[0].size();
        for (int i = 0; i < (m + 1) / 2 && i < (n + 1) / 2; i++) {
            if (i == m - 1 - i) {
                for(int j = i; j < n - i; j++) {
                    ans.push_back(matrix[i][j]);
                }
                break;
            }
            if (i == n - 1 - i) {
                for (int j = i; j <= m - 1 - i; j++) {
                    ans.push_back(matrix[j][i]);
                }
                break;
            }
            for (int j = i; j < n - i; j++) {
                ans.push_back(matrix[i][j]);
            }
            for (int j = i + 1; j < m - 1 - i; j++) {
                ans.push_back(matrix[j][n - 1 - i]);
            }
            for (int j = n - 1 - i; j >= i; j--) {
                ans.push_back(matrix[m - 1 - i][j]);
            }
            for (int j = m - 1 - i - 1; j > i; j--) {
                ans.push_back(matrix[j][i]);
            }
        }
        return ans;
    }
};