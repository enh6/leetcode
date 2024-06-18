class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # result[i] = product of nums[i+1] , nums[i+2], ...
        for i in range(len(nums)-2, -1, -1):
            result[i] = result[i+1] * nums[i+1]
        left_prod = 1
        for i in range(len(nums)):
            if i-1 >= 0:
                left_prod = left_prod * nums[i-1]
            result[i] = left_prod * result[i]
        return result
