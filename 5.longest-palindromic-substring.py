class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pos = 0
        n = 1
        for i in range(len(s)):
            left, right = i - 1, i + 1
            while right < len(s) and s[i] == s[right]:
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > n:
                pos = left + 1
                n = right - left - 1
        return s[pos:pos + n]