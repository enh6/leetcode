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

    void dfs(vector<int>& pos, int cur, int& ans) {
        int n = pos.size();
        for (int i = 0; i < n; i++) {
            if (!valid(pos, cur, i)) {
                continue;
            }
            pos[cur] = i;
            if (cur < n - 1) {
                dfs(pos, cur + 1, ans);
            } else {
                ans++;
            }
        }
    }

    int totalNQueens(int n) {
        int ans = 0;
        vector<int> pos(n, -1);
        dfs(pos, 0, ans);
        return ans;
    }
};