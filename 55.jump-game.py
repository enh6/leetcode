class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        i = 0
        while i < len(nums) and i <= max_pos:
            max_pos = max(max_pos, i + nums[i])
            i += 1
        return max_pos >= len(nums) - 1