class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = (dividend < 0) != (divisor < 0)
        ret = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            n = 1
            div = divisor
            while dividend >= div + div:
                div = div + div
                n = n + n
            dividend -= div
            ret += n
        if sign:
            ret = -ret
        if ret < -2**31 or ret > 2**31-1:
            return 2**31-1
        else:
            return ret