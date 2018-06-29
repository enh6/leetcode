class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        ans.push_back({});
        for (int i = 0; i < nums.size(); i++) {
            int n = ans.size();
            for (int j = 0; j < n; j++) {
                auto a = ans[j];
                a.push_back(nums[i]);
                ans.push_back(a);
            }
            int k = 1;
            while (i + 1 < nums.size() && nums[i + 1] == nums[i]) {
                for (int j = 0; j < n; j++) {
                    auto a = ans[k * n + j];
                    a.push_back(nums[i]);
                    ans.push_back(a);
                }
                k++;
                i++;
            }
        }
        return ans;
    }
};