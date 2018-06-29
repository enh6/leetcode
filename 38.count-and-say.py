class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = [1]
        for _ in range(n - 1):
            nums2 = []
            i = 0
            while i < len(nums):
                j = 1;
                while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    j += 1
                    i += 1
                nums2.append(j)
                nums2.append(nums[i])
                i += 1
            nums = nums2
        return "".join(str(i) for i in nums)