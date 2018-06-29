class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [_ for _ in range(n + 1)]
        for i in range(1, m + 1):
            pre = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                cur = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = pre
                else:
                    dp[j] = min(pre, dp[j], dp[j - 1]) + 1
                pre = cur
        return dp[n]