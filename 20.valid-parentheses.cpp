class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (auto c: s) {
            if (c == '(' || c == '{' || c == '[') {
                stk.push(c);
            } else if (c == ')') {
                if (!stk.empty() && stk.top() == '(') {
                    stk.pop();
                } else {
                    return false;
                }
            } else if (c == ']') {
                if (!stk.empty() && stk.top() == '[') {
                    stk.pop();
                } else {
                    return false;
                }
            } else if (c == '}') {
                if (!stk.empty() && stk.top() == '{') {
                    stk.pop();
                } else {
                    return false;
                }
            }
        }
        return stk.empty();
    }
};