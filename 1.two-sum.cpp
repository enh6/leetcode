class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> int_map;
        for (int i = 0; i < nums.size(); i++) {
            auto iter = int_map.find(target - nums[i]);
            if (iter == int_map.end()) {
                int_map[nums[i]] = i;
            } else {
                return vector<int>{iter->second, i};
            }
        }
    }
};