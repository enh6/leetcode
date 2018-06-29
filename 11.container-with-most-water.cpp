class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_area = 0;
        int i = 0, j = height.size() - 1;
        while (i < j) {
            max_area = max(max_area, min(height[i], height[j]) * (j - i));
            height[i] > height[j] ? j-- : i++;
        }
        return max_area;
    }
};