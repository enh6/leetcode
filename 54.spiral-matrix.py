class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        m = len(matrix)
        if m == 0:
            return ans
        n = len(matrix[0])
        i = 0
        while i < m / 2 and i < n / 2:
            if i == m - 1 - i:
                ans += matrix[i][i:n - i]
                break
            if i == n - 1 - i:
                ans += [matrix[j][i] for j in range(i, m - i)]
                break
            ans += matrix[i][i:n - i]
            ans += [matrix[j][n - 1 - i] for j in range(i + 1, m - 1 - i)]
            ans += matrix[m - 1 - i][- 1 - i:i - 1 - n:-1]
            ans += [matrix[j][i] for j in range(m - 1 - i - 1, i, -1)]
            i += 1
        return ans;