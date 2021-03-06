class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        tmp = nums[i - 1]
                        nums[i - 1] = nums[j]
                        nums[j] = tmp
                        j, k = i, len(nums) - 1
                        while j < k:
                            tmp = nums[j]
                            nums[j] = nums[k]
                            nums[k] = tmp
                            j += 1
                            k -= 1
                        return
        nums.reverse()
        return

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [];
        ans.append(nums[:])
        n = 1
        for i in range(len(nums)):
            n = n * (i + 1);
        for _ in range(1, n):
            self.nextPermutation(nums)
            ans.append(nums[:])
        return ans