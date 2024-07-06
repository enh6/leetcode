class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        result = 0
        i = 0
        l = -1
        while i + 1 < len(nums):
            if nums[i] == k/2:
                j = i + 1
                while j < len(nums) and nums[j] == k/2:
                    j = j + 1
                result = result + (j - i) // 2
                l = i - 1
                r = j
                break
            elif nums[i] < k/2 and nums[i+1] > k/2:
                l = i
                r = i + 1
                break
            else:
                i = i + 1
        while l >= 0 and r < len(nums):
            s = nums[l] + nums[r]
            if s == k:
                result = result + 1
                l = l - 1
                r = r + 1
            elif s > k:
                l = l - 1
            else:
                r = r + 1
        return result
