class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, len(nums) - 1
        while w <= b:
            if nums[w] == 0:
                nums[w] = nums[r]
                nums[r] = 0
                r += 1
                w += 1
            elif nums[w] == 2:
                nums[w] = nums[b]
                nums[b] = 2
                b -= 1
            else:
                w += 1