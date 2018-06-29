class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        ans = [0] * (m + n)
        num1 = [int(x) for x in reversed(num1)]
        num2 = [int(x) for x in reversed(num2)]
        for i in range(m):
            carry = 0
            for j in range(n):
                num = ans[i + j] + num1[i] * num2[j] + carry
                ans[i + j] = num % 10
                carry = num // 10
            ans[i + n] += carry
        ans = "".join(str(x) for x in reversed(ans)).lstrip('0')
        return ans or '0'