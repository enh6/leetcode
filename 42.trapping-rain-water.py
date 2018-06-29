class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trap = 0
        max_height = 0
        max_height_pos = 0
        for i, h in enumerate(height):
            if h > max_height:
                max_height = h
                max_height_pos = i
        max_h = 0
        for h in height[:max_height_pos]:
            if h > max_h:
                max_h = h
            else:
                trap += (max_h - h)
        max_h = 0
        for h in height[-1:max_height_pos:-1]:
            if h > max_h:
                max_h = h
            else:
                trap += (max_h - h)
        return trap