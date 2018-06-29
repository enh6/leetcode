class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> table(m, vector<int>(n));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j]) {
                    table[i][j] = 0;
                } else if (i == 0 && j == 0) {
                    table[i][j] = 1;
                } else if (i == 0) {
                    table[i][j] = table[i][j - 1];
                } else if (j == 0) {
                    table[i][j] = table[i - 1][j];
                } else {
                    table[i][j] = table[i][j - 1] + table[i - 1][j];
                }
            }
        }
        return table[m - 1][n - 1];
    }
};