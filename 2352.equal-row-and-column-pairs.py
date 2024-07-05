class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = [hash(str(r)) for r in grid]
        cols = [hash(str([grid[j][i] for j in range(n)])) for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(n):
                if rows[i] == cols[j]:
                    result = result + 1
        return result
