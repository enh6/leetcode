class Solution {
public:
    int minFlips(int a, int b, int c) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            int aa = (a >> i) & 1;
            int bb = (b >> i) & 1;
            int cc = (c >> i) & 1;
            if ((aa || bb) == cc) {
                continue;
            } else if (cc == 1) {
                count++;
            } else {
                count+=(aa+bb);
            }
        }
        return count;
    }
};