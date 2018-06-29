class Solution {
public:
    string addBinary(string a, string b) {
        if (a.length() < b.length()) {
            swap(a, b);
        }
        int c = 0;
        for (int i = a.length() - 1, j = b.length() - 1; i >= 0; i--, j--) {
            if (a[i] == '1') {
                c++;
            }
            if (j >= 0 && b[j] == '1') {
                c++;
            }
            a[i] = c % 2 ? '1' : '0';
            c = c / 2;
        }
        if (c) {
            return "1" + a;
        } else {
            return a;
        }
    }
};