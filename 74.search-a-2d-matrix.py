class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False;
        n = len(matrix[0])
        i, j = 0, len(matrix) - 1
        while i <= j:
            mid = (i + j) >> 1
            if matrix[mid][0] > target:
                j = mid - 1
            elif matrix[mid][n - 1] < target:
                i = mid + 1
            else:
                i, j = 0, n - 1
                while i <= j:
                    mid2 = (i + j) >> 1
                    if matrix[mid][mid2] > target:
                        j = mid2 - 1
                    elif matrix[mid][mid2] < target:
                        i = mid2 + 1
                    else:
                        return True
        return False