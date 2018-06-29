class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int ans = 0;
        stack<int> index;
        for (int i = 0; i <= heights.size(); i++) {
            while (!index.empty() && (i == heights.size() || heights[index.top()] > heights[i])) {
                int h = heights[index.top()];
                index.pop();
                if (index.empty()) {
                    ans = max(ans, h * i);
                } else {
                    ans = max(ans, h * (i - index.top() - 1));
                }
            }
            index.push(i);
        }
        return ans;
    }
};