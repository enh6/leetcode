class Solution {
public:
    bool valid(vector<int>& pos, int cur, int i) {
        for (int j = 0; j < cur; j++) {
            if (pos[j] == i || pos[j] - i == j - cur || pos[j] - i == cur - j) {
                return false;
            }
        }
        return true;
    }
    void dfs(vector<int>& pos, int cur, vector<vector<string>>& ans) {
        int n = pos.size();
        for (int i = 0; i < n; i++) {
            if (!valid(pos, cur, i)) {
                continue;
            }
            pos[cur] = i;
            if (cur < n - 1) {
                dfs(pos, cur + 1, ans);
            } else {
                vector<string> vs(n, string(n, '.'));
                for (int k = 0; k < n; k++) {
                    vs[k][pos[k]] = 'Q';
                }
                ans.push_back(vs);
            }
        }
    }

    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        vector<int> pos(n, -1);
        dfs(pos, 0, ans);
        return ans;
    }
};