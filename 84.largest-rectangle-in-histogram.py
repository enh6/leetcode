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