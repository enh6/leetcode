class Solution {
public:
    void combination(vector<int>& candidates, int target, int pos, vector<int>& current, vector<vector<int>>& ans) {
        if (target == 0) {
            ans.push_back(current);
            return;
        }
        if (target < 0) {
            return;
        }
        for (int i = pos; i < candidates.size(); i++) {
            current.push_back(candidates[i]);
            combination(candidates, target - candidates[i], i, current, ans);
            current.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> current;
        sort(candidates.rbegin(), candidates.rend());
        combination(candidates, target, 0, current, ans);
        return ans;
    }
};