class Solution {
public:
    void find(int* nums, int idx, int k, int n, vector<vector<int>> &ret) {
        if (k == 0 && n == 0) {
            vector<int> v;
            for (int i = 0; i < 9; i++) {
                if (nums[i] > 0) {
                    v.push_back(nums[i]);
                }
            }
            ret.push_back(v);
            return;
        }
        if (idx >= 9) {
            return;
        }
        find(nums, idx+1, k, n, ret);
        nums[idx] = idx+1;
        find(nums, idx+1, k-1, n-nums[idx], ret);
        nums[idx] = 0;
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        int nums[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
        vector<vector<int>> ret;
        find(nums, 0, k, n, ret);
        return ret;
    }
};
