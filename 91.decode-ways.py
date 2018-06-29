class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        last = 1
        before_last = 1
        for i in range(1, len(s)):
            cur = 0
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6' and s[i] >= '0'):
                if s[i] != '0':
                    cur = last + before_last
                else:
                    cur = before_last
            elif s[i] == '0':
                return 0
            else:
                cur = last
            before_last = last
            last = cur
        return last