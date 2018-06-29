class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> map(128, 0);
        for (auto c : t) {
            map[c]++;
        }
        int begin = 0, end = 0, count = 0;
        int window_head = 0, window_length = s.length() + 1;
        while (end < s.size()) {
            map[s[end]]--;
            if (map[s[end]] >= 0) {
                count++;
            }
            if (count == t.length()) {
                while (map[s[begin]] < 0) {
                    map[s[begin]]++;
                    begin++;
                }
                if (end - begin + 1 < window_length) {
                    window_length = end - begin + 1;
                    window_head = begin;
                }
                map[s[begin]]++;
                begin++;
                count--;
            }
            end++;
        }
        return window_length > s.length() ? "" : s.substr(window_head, window_length);
    }
};