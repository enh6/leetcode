class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        for i in range(0, n // 2):
            for j in range(i, n - i):
                ans[i][j] = num
                num += 1
            for j in range(i + 1, n - 1 - i):
                ans[j][n - 1 - i] = num
                num += 1
            for j in range(n - 1 - i, i - 1, -1):
                ans[n - 1 - i][j] = num
                num+= 1
            for j in range(n - 1 - i - 1, i, -1):
                ans[j][i] = num
                num += 1
        if n % 2:
            ans[n // 2][n // 2] = num
        return ans