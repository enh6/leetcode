class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        sum = 0
        for num in nums:
            sum = max(sum, 0)
            sum += num
            ans = max(ans, sum)
        return ans