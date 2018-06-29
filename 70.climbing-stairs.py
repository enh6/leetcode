class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur = 1
        last = 1
        for _ in range(n - 1):
            tmp = cur + last
            last = cur
            cur = tmp
        return cur