class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int prev_ones = 0;
        int cur_ones = 0;
        int result = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                cur_ones++;
            } else {
                if (prev_ones + cur_ones > result) {
                    result = prev_ones + cur_ones;
                }
                prev_ones = cur_ones;
                cur_ones = 0;
            }
        }

        // all ones
        if (result == 0 && cur_ones == nums.size()) {
            return nums.size() - 1;
        }

        if (prev_ones + cur_ones > result) {
            result = prev_ones + cur_ones;
        }
        return result;
    }
};