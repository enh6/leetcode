class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        while x:
            r = r * 10 + x % 10
            x = x // 10
        return 0 if r < -2147483648 or r > 2147483647 else r;