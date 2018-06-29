class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = nums[0] + nums[1] + nums[2];
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < abs(closest - target):
                    closest = sum
                if sum > target:
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    return target
        return closest