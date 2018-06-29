class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        ans = self.grayCode(n - 1)
        s = len(ans)
        for i in range(s - 1, -1, -1):
            ans.append(s + ans[i])
        return ans