class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return [[]]
        if k == n:
            return [[i for i in range(1, n + 1)]]
        ans1 = self.combine(n - 1, k)
        ans2 = self.combine(n - 1, k - 1)
        for a in ans2:
            a.append(n)
            ans1.append(a)
        return ans1