class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        co = [0] * (m + n - 1)
        co[0] = 1
        for i in range(1, m + n - 1):
            for j in range(i, 0, -1):
                co[j] = co[j] + co[j - 1]
        return co[m - 1]