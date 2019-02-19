class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t or len(s) < len(t):
            return 0
        dp = [0] * len(t)
        if s[0] == t[0]:
            dp[0] = 1
        for i in range(1, len(s)):
            for j in range(len(t) - 1, 0, -1):
                if s[i] == t[j]:
                    dp[j] = dp[j] + dp[j-1]
            if s[i] == t[0]:
                dp[0] += 1
        return dp[-1]
