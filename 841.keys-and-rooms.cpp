class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        vector<int> visited(n, 0);
        vector<int> keys = rooms[0];
        visited[0] = 1;
        while (!keys.empty()) {
            vector<int> new_keys;
            for (int key : keys) {
                if (!visited[key]) {
                    visited[key] = 1;
                    new_keys.insert(new_keys.end(), rooms[key].begin(), rooms[key].end());
                }
            }
            keys = new_keys;
        }
        return accumulate(visited.begin(), visited.end(), 0) == n;
    }
};