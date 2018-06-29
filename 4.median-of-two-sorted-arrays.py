class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)
        c = (m + n) // 2
        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            if mid < n and nums1[c - mid - 1] > nums2[mid]:
                low = mid + 1
            elif mid - 1 >= 0 and nums1[c - mid] < nums2[mid - 1]:
                high = mid - 1
            else:
                high = low = mid
        a = min(nums2[low] if low < n else sys.maxsize, nums1[c - low] if c - low < m else sys.maxsize)
        if ((m + n) % 2 == 1):
            return a
        b = max(nums2[low - 1] if low - 1 >= 0 else -sys.maxsize, nums1[c - low - 1] if c - low - 1 >= 0 else -sys.maxsize)
        return (a + b) / 2
