class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i = 1
        for j in nums[2:]:
            if j != nums[i - 1]:
                i += 1
                nums[i] = j
        return i + 1