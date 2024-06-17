class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            mid = len(nums) // 2
            a = self.findMin(nums[:mid])
            b = self.findMin(nums[mid:])
            if a < b:
                return a
            else:
                return b
