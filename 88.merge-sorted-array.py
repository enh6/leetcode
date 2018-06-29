class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        m -= 1
        n -= 1
        while n >= 0:
            if m < 0 or nums2[n] > nums1[m]:
                nums1[pos] = nums2[n]
                n -= 1
            else:
                nums1[pos] = nums1[m]
                m -= 1
            pos -= 1