class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        nums.sort()
        l = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(ans)
            for j in ans[-l:]:
                ans.append(j + [nums[i]])
        return ans