class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return false;
        }
        int n = matrix[0].size();
        int i = 0, j = matrix.size() - 1;
        while (i <= j) {
            int mid = (i + j) / 2;
            if (matrix[mid][0] > target) {
                j = mid - 1;
            } else if (matrix[mid][n - 1] < target) {
                i = mid + 1;
            } else {
                i = 0, j = n - 1;
                while (i <= j) {
                    int mid2 = (i + j) / 2;
                    if (matrix[mid][mid2] > target) {
                        j = mid2 - 1;
                    } else if (matrix[mid][mid2] < target) {
                        i = mid2 + 1;
                    } else {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};