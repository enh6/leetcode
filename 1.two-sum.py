class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        int_dict = {}
        for index, num in enumerate(nums):
            if target - num in int_dict:
                return [int_dict[target - num], index]
            else:
                int_dict[num] = index
