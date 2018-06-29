class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
        for i in range(1, n):
            grid[0][i] = grid[0][i - 1] + grid[0][i]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]
        return grid[-1][-1]