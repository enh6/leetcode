class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_in_first_col = False
        zero_in_first_row = False
        for i in range(m):
            if matrix[i][0] == 0:
                zero_in_first_col = True
                break
        for i in range(n):
            if matrix[0][i] == 0:
                zero_in_first_row = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zero_in_first_col:
            for i in range(m):
                matrix[i][0] = 0
        if zero_in_first_row:
            for i in range(n):
                matrix[0][i] = 0