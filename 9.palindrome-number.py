class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        r = 0
        while r < x:
            r = r * 10 + x % 10
            x = x // 10
        return r == x or r // 10 == x