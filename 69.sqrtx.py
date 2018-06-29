class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = x
        while ans * ans > x:
            ans = (ans + x // ans) // 2
        return ans