class Solution:
    def add(self, ret, s, n, m):
        if n > m:
            return
        if m == 0 and n == 0:
            ret.append(s)
        if n > 0:
            self.add(ret, s + '(', n - 1, m)
        if m > 0:
            self.add(ret, s + ')', n, m - 1)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.add(ret, "", n, n)
        return ret