class Solution {
public:
    string simplifyPath(string path) {
        path += "/";
        vector<string> paths;
        int start = 0, end;
        while ((end = path.find('/', start + 1)) != string::npos) {
            string token = path.substr(start, end - start);
            if (token != "/.." && token != "/." && token != "/") {
                paths.push_back(token);
            } else if (token == "/.." && !paths.empty()) {
                paths.pop_back();
            }
            start = end;
        }
        string ans;
        for (const auto& s : paths) {
            ans += s;
        }
        return ans.empty() ? "/" : ans;
    }
};