class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> co(m + n - 1, 0);
        co[0] = 1;
        for (int i = 1; i < m + n - 1; i++) {
            for (int j = i; j > 0; j--) {
                co[j] = co[j] + co[j - 1];
            }
        }
        return co[m - 1];
    }
};