class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        v = [0] * (n + 1)
        v[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                v[i] += v[j] * v[i - j - 1]
        return v[n]