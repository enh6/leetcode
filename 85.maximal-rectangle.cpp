class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int ans = 0;
        stack<int> index;
        for (int i = 0; i <= heights.size(); i++) {
            while (!index.empty() && (heights[index.top()] > heights[i] || i == heights.size())) {
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

    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) {
            return 0;
        }
        int ans = 0;
        vector<int> heights(matrix[0].size(), 0);
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == '1') {
                    heights[j]++;
                } else {
                    heights[j] = 0;
                }
            }
            ans = max(ans, largestRectangleArea(heights));
        }
        return ans;
    }
};