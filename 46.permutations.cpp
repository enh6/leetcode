class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        for (int i = nums.size() - 1; i > 0; i--) {
            if (nums[i - 1] < nums[i]) {
                for (int j = nums.size() - 1; j >= i; j--) {
                    if (nums[j] > nums[i - 1]) {
                        int tmp = nums[i - 1];
                        nums[i - 1] = nums[j];
                        nums[j] = tmp;
                        reverse(nums.begin() + i, nums.end());
                        return;
                    }
                }
            }
        }
        reverse(nums.begin(), nums.end());
        return;
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        ans.push_back(nums);
        int n = 1;
        for (int i = 1; i <= nums.size(); i++) {
            n = n * i;
        }
        for (int i = 1; i < n; i++) {
            nextPermutation(nums);
            ans.push_back(nums);
        }
        return ans;
    }
};