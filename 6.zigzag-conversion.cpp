class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        string z;
        for (int i = 0; i < numRows; i++) {
            for (int j = i; j < s.length(); j += 2 * numRows - 2) {
                z += s[j];
                if (i != 0 && i != numRows - 1 && j + 2 * (numRows - i - 1) < s.length()) {
                    z += s[j + 2 * (numRows - i - 1)];
                }
            }
        }
        return z;
    }
};