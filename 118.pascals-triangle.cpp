class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
        vector<int> row;
        for (int i = 0; i < numRows; i++) {
            row.push_back(1);
            for (int j = row.size() - 2; j > 0; j--) {
                row[j] = row[j - 1] + row[j];
            }
            ans.push_back(row);
        }
        return ans;
    }
};
