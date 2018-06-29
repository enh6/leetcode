class Solution {
public:
    int climbStairs(int n) {
        int cur = 1, last = 1;
        while (--n) {
            int tmp = cur + last;
            last = cur;
            cur = tmp;
        }
        return cur;
    }
};