class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x_len = len(matrix[0])
        y_len = len(matrix)
        return self._search(matrix, 0, x_len, 0, y_len, target)

    def _search(self, matrix, left, right, up, down, target):
        if right - left < 1 or down - up < 1:
            return False
        if right - left == 1 and down - up == 1:
            return matrix[up][left] == target
        x_mid = (right + left) // 2
        y_mid = (down + up) // 2
        val = matrix[y_mid][x_mid]
        if val == target:
            return True
        elif val > target:
            if self._search(matrix, left, x_mid, up, y_mid, target):
                return True
            if self._search(matrix, left, x_mid, y_mid, down, target):
                return True
            if self._search(matrix, x_mid, right, up, y_mid, target):
                return True
            return False
        else:
            if self._search(matrix, x_mid + 1, right, y_mid + 1, down, target):
                return True
            if self._search(matrix, left, x_mid + 1, y_mid + 1, down, target):
                return True
            if self._search(matrix, x_mid + 1, right, up, y_mid + 1, target):
                return True
            return False
