class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int> right_sum;
        right_sum.push_back(0);
        int sum = 0;
        for (int i = nums.size() - 2; i >= 0; i--) {
            sum += nums[i+1];
            right_sum.push_back(sum);
        }
        if (right_sum[nums.size() - 1] == 0) {
            return 0;
        }

        sum = 0;
        for (int i = 1; i < nums.size(); i++) {
            sum += nums[i-1];
            if (sum == right_sum[nums.size() - 1 - i]) {
                return i;
            }
        }
        return -1;
    }
};