class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums) < 4:
            return ret
        nums.sort()
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                t = target - nums[i] - nums[j]
                k, l = j + 1,len(nums) - 1
                while k < l:
                    if nums[k] + nums[l] == t:
                        ret.append([nums[i], nums[j], nums[k], nums[l]])
                        while k < l and nums[k + 1] == nums[k]:
                            k += 1
                        while k < l and nums[l - 1] == nums[l]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif nums[k] + nums[l] > t:
                        l -= 1
                    else:
                        k += 1
                while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                    j += 1
                j += 1
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            i += 1
        return ret