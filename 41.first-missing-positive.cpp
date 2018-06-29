class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            while (nums[i] - 1 >= 0 && nums[i] - 1 < nums.size() && nums[nums[i] - 1] != nums[i]) {
                int tmp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = tmp;
            }
        }
        int j;
        for (j = 0; j < nums.size(); j++) {
            if (nums[j] - 1 != j) {
                break;
            }
        }
        return j + 1;
    }
};