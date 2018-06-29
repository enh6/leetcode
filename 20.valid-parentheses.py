class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stk.append(c);
            elif c == ')':
                if len(stk) == 0 or stk.pop() != '(':
                    return False
            elif c == ']':
                if len(stk) == 0 or stk.pop() != '[':
                    return False
            elif c == '}':
                if len(stk) == 0 or stk.pop() != '{':
                    return False
        return len(stk) == 0