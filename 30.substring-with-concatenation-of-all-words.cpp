class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ret;
        int wl = words[0].length();
        int wc = words.size();
        if (s.length() < wl * wc) {
            return ret;
        }
        map<string, int> occurs;
        for (auto& w : words) {
            occurs[w]++;
        }
        for (int i = 0; i <= s.length() - wl * wc; i++) {
            map<string, int> occ;
            int cnt = 0;
            for (int j = 0; j < wc; j++) {
                string w = s.substr(i + j * wl, wl);
                if (occurs.find(w) == occurs.end()) {
                    break;
                } else {
                    occ[w]++;
                    if (occ[w] == occurs[w]) {
                        cnt++;
                    } else if (occ[w] > occurs[w]) {
                        break;
                    }
                }
            }
            if (cnt == occurs.size()) {
                ret.push_back(i);
            }
        }
        return ret;
    }
};