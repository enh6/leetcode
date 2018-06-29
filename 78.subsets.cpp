class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        ans.push_back({});
        for (int i = 0; i < nums.size(); i++) {
            int n = ans.size();
            for (int j = 0; j < n; j++) {
                auto a = ans[j];
                a.push_back(nums[i]);
                ans.push_back(a);
            }
        }
        return ans;
    }
};