class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_length = 0;
        int begin = -1;
        vector<int> map(256, -1);
        for (int end = 0; end < s.length(); end++) {
            if (map[s[end]] > begin) {
                begin = map[s[end]];
            }
            map[s[end]] = end;
            max_length = max(max_length, end - begin);
        }
        return max_length;
    }
};
