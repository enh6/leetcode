class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ret;
        if (nums.size() < 4) {
            return ret;
        }
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 3; i++) {
            for (int j = i + 1; j < nums.size() - 2; j++) {
                int t = target - nums[i] - nums[j];
                int k = j + 1, l = nums.size() - 1;
                while (k < l) {
                    if (nums[k] + nums[l] == t) {
                        ret.push_back(vector<int>{nums[i], nums[j], nums[k], nums[l]});
                        while (k < l && nums[k + 1] == nums[k]) {
                            k++;
                        }
                        while (k < l && nums[l - 1] == nums[l]) {
                            l--;
                        }
                        k++;
                        l--;
                    } else if (nums[k] + nums[l] > t) {
                        l--;
                    } else {
                        k++;
                    }
                }
                while (j + 1 < nums.size() && nums[j + 1] == nums[j]) {
                    j++;
                }
            }
            while (i + 1 < nums.size() && nums[i + 1] == nums[i]) {
                i++;
            }
        }
        return ret;
    }
};