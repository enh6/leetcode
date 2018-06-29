class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(p):
            if j + 1 < len(p) and p[j + 1] == '*':
                if self.isMatch(s[i:], p[j + 2:]):
                    return True
                k = 0
                while i + k < len(s) and (s[i + k] == p[j] or p[j] == '.'):
                    if self.isMatch(s[i + k + 1:], p[j + 2:]):
                        return True
                    k += 1
                return False
            elif i < len(s) and (p[j] == s[i] or p[j] == '.'):
                i += 1
                j += 1
            else:
                return False
        return i == len(s)
