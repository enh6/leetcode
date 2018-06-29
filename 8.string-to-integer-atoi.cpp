class Solution {
public:
    int myAtoi(string str) {
        auto it  = find_if_not(str.begin(), str.end(), ::isspace);
        if (it == str.end()) {
            return 0;
        }
        long long r = 0;
        int sign = 1;
        if (*it == '+') {
            it++;
        } else if (*it == '-') {
            it++;
            sign = -1;
        }
        if (it == str.end() || !isdigit(*it)) {
            return 0;
        }
        while(it != str.end() && isdigit(*it)) {
            r = r * 10 + (*it - '0');
            it++;
            if (sign * r > INT_MAX) {
                return INT_MAX;
            } else if (sign * r < INT_MIN) {
                return INT_MIN;
            }
        }
        return sign * r;
    }
};