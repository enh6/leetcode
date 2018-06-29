class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n + 1) // 2):
            for j in range(n  // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1  -j]
                matrix[n - 1 - i][n - 1  -j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp