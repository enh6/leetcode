class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        index = []
        for i in range(len(heights) + 1):
            while index and (i == len(heights) or heights[index[-1]] > heights[i]):
                h = heights[index.pop()]
                if not index:
                    ans = max(ans, h * i)
                else:
                    ans = max(ans, h * (i - index[-1] - 1))
            index.append(i)
        return ans;

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        ans = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans