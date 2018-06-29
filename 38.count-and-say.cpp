class Solution {
public:
    string countAndSay(int n) {
        vector<int> nums = { 1 };
        while (--n) {
            vector<int> nums2;
            for (int i = 0; i < nums.size(); i++) {
                int j = 1;
                while (i + 1 < nums.size() && nums[i] == nums[i + 1]) {
                    j++;
                    i++;
                }
                nums2.push_back(j);
                nums2.push_back(nums[i]);
            }
            nums = nums2;
        }
        string s;
        for (int n : nums) {
            s += ('0' + n);
        }
        return s;
    }
};