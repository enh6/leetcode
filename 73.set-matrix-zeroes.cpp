class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        bool zero_in_first_col = false;
        bool zero_in_first_row = false;
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                zero_in_first_col = true;
                break;
            }
        }
        for (int i = 0; i < n; i++) {
            if (matrix[0][i] == 0) {
                zero_in_first_row = true;
                break;
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        if (zero_in_first_col) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
        if (zero_in_first_row) {
            for (int i = 0; i < n; i++) {
                matrix[0][i] = 0;
            }
        }
    }
};