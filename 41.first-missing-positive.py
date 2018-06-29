class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] - 1 >= 0 and nums[i] - 1 < len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
        j = 0
        while j < len(nums):
            if nums[j] - 1 != j:
                break
            j += 1
        return j + 1