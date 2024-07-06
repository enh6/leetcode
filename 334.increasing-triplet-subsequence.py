class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = nums[0]
        b = 2**31
        i = 1
        for i in range(1, len(nums)):
            n = nums[i]
            if n > a and n < b:
                b = n
            elif n > b:
                return True
            elif n < a:
                a = n
        return False
