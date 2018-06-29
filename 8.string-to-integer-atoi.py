class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if len(str) == 0:
            return 0
        i = 0
        sign = 1
        r = 0
        if str[0] == '+':
            i += 1
        elif str[0] == '-':
            i += 1
            sign = -1
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
            r = r * 10 + ord(str[i]) - ord('0')
            i += 1
            if sign * r > 2 ** 31 - 1:
                return 2147483647
            elif sign * r < - 2 ** 31:
                return -2147483648
        return sign * r