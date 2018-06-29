class Solution {
public:
    int trap(vector<int>& height) {
        int trap = 0;
        int max_height = 0, max_height_pos = 0;
        for (int i = 0; i < height.size(); i++) {
            if (height[i] > max_height) {
                max_height = height[i];
                max_height_pos = i;
            }
        }
        for (int max_h = 0, i = 0; i < max_height_pos; i++) {
            int h = height[i];
            if (h > max_h) {
                max_h = h;
            } else {
                trap += (max_h - h);
            }
        }
        for (int max_h = 0, i = height.size() - 1; i > max_height_pos; i--) {
            int h = height[i];
            if (h > max_h) {
                max_h = h;
            } else {
                trap += (max_h - h);
            }
        }
        return trap;
    }
};