class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for i in nums:
            for j in range(len(ans)):
                a = ans[j][:]
                a.append(i)
                ans.append(a)
        return ans