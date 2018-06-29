class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.size();
        int n = num2.size();
        string ans(m + n, '0');
        reverse(num1.begin(),num1.end());
        reverse(num2.begin(),num2.end());
        for(int i = 0; i < m; i++) {
            int carry = 0;
            for(int j = 0; j < n; j++) {
                int num = (ans[i + j] - '0') + (num1[i] - '0') * (num2[j] - '0') + carry;
                ans[i + j] = num % 10 + '0';
                carry = num / 10;
            }
            ans[i + n] += carry;
        }
        reverse(ans.begin(), ans.end());
        auto pos = ans.find_first_not_of('0');
        return pos == string::npos ? "0" : ans.substr(pos);
    }
};