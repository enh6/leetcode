class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }
        int prev_prev = nums[0];
        int prev = nums[1] > nums[0] ? nums[1] : nums[0];
        for (int i = 2; i < n; i++) {
            int cur = prev_prev + nums[i];
            if (prev > cur) {
                cur = prev;
            }
            prev_prev = prev;
            prev = cur;
        }
        return prev;
    }
};
