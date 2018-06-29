class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        m = len(s)
        n = len(p)
        match_pos = -1
        pattern_pos = -1
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                j += 1
                pattern_pos = j
                match_pos = i
            elif pattern_pos != -1:
                j = pattern_pos
                match_pos += 1
                i = match_pos
            else:
                return False
        while j < n and p[j] == '*':
            j += 1
        return j == n