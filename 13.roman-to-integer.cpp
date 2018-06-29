class Solution {
public:
    int romanToInt(string s) {
        int r = 0;
        map<char, int> m{
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        for(auto iter = s.begin(); iter != s.end(); iter++) {
            if ((iter + 1) != s.end() && m[*iter] < m[*(iter + 1)]) {
                r -= m[*iter];
            } else {
                r += m[*iter];
            }
        }
        return r;
    }
};