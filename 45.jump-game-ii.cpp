class Solution {
public:
    int jump(vector<int>& nums) {
        int max_pos = 0;
        int min_pos = 0;
        int step = 0;
        while (max_pos < nums.size() - 1) {
            step++;
            int next_max_pos = max_pos + 1;
            for (int i = min_pos; i <= max_pos; i++) {
                next_max_pos = max(next_max_pos, i + nums[i]);
            }
            min_pos = max_pos + 1;
            max_pos = next_max_pos;
        }
        return step;
    }
};