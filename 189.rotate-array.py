class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self._rotate(nums, len(nums), k)

    def _rotate(self, nums: List[int], l: int, k: int) -> None:
        k = k % l
        if k == 0:
            return
        for i in range(k):
            idx = l - 1 - i
            tmp = nums[idx]
            while idx - k >= 0:
                nums[idx] = nums[idx - k]
                idx = idx - k
            nums[idx] = tmp
        mod = l % k
        if mod > 0:
            self._rotate(nums, k, k - mod)
