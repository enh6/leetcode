class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        pos = [None] * n
        def valid(cur, i):
            for j in range(cur):
                if pos[j] == i or pos[j] - i == j - cur or pos[j] - i == cur - j:
                    return False
            return True
        def dfs(cur):
            n = len(pos)
            for i in range(n):
                if not valid(cur, i):
                    continue
                pos[cur] = i
                if cur < n - 1:
                    dfs(cur + 1)
                else:
                    self.ans += 1
        dfs(0)
        return self.ans