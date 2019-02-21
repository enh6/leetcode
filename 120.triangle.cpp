class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<int> sums = triangle[0];
        for (int i = 1; i < triangle.size(); i++) {
            vector<int> row = triangle[i];
            int len = row.size();
            vector<int> new_sums(len);
            new_sums[0] = sums[0] + row[0];
            for (int j = 1; j < len - 1; j++) {
                new_sums[j] = min(sums[j - 1], sums[j]) + row[j];
            }
            new_sums[len - 1] = sums[len - 2] + row[len - 1];
            sums = new_sums;
        }
        return *min_element(sums.begin(), sums.end());
    }
};
