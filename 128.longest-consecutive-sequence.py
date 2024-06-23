class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        vals = {}
        maxval = 0
        for n in nums:
            x = vals[n-1] if n-1 in vals else 0
            y = vals[n+1] if n+1 in vals else 0
            val = x + y + 1
            vals[n-x] = val
            vals[n+y] = val
            maxval = max(maxval, val)
        return maxval
