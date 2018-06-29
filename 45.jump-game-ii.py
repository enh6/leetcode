class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_pos = 0
        min_pos = 0
        step = 0
        while max_pos < len(nums) - 1:
            step += 1
            next_max_pos = max_pos + 1
            for i in range(min_pos, max_pos + 1):
                next_max_pos = max(next_max_pos, i + nums[i])
            min_pos = max_pos + 1
            max_pos = next_max_pos
        return step