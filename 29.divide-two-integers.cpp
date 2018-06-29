class Solution {
public:
    int divide(int dividend, int divisor) {
        bool sign = (dividend < 0) ^ (divisor < 0);
        long long ll_dividend = labs(dividend);
        long long ll_divisor = labs(divisor);
        long long ret = 0;
        while (ll_dividend >= ll_divisor) {
            long long n = 1;
            long long div = ll_divisor;
            while (ll_dividend >= div + div) {
                div = div + div;
                n = n + n;
            }
            ll_dividend -= div;
            ret += n;
        }
        if (sign) {
            ret = -ret;
        }
        if (ret < INT_MIN || ret > INT_MAX) {
            return INT_MAX;
        } else {
            return ret;
        }
    }
};