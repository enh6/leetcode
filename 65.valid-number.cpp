class Solution {
public:
    bool isNumber(string s) {
        // \s* space
        // \d+(\.\d*)?|\.\d+ float
        // [+-]?\\d+ integer
        regex rg(R"(\s*[+-]?(\d+(\.\d*)?|\.\d+)(e[+-]?\d+)?\s*)");
        return std::regex_match(s, rg);
    }
};