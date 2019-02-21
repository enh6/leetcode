class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row;
        for (int i = 0; i <= rowIndex; i++) {
            row.push_back(1);
            for (int j = row.size() - 2; j > 0; j--) {
                row[j] = row[j - 1] + row[j];
            }
        }
        return row;
    }
};
