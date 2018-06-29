class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        return i + 1