class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        if (m < n) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int c = (m + n) / 2;
        int low = 0, high = n;
        while(low < high) {
            int mid = (low + high) / 2;
            if (mid < n && nums1[c - mid - 1] > nums2[mid]) {
                low = mid + 1;
            } else if (mid - 1 >= 0 && nums1[c - mid] < nums2[mid - 1]) {
                high = mid - 1;
            } else {
                high = low = mid;
            }
        }
        int a = min(low >= n ? INT_MAX : nums2[low], c - low >= m ? INT_MAX : nums1[c - low]);
        if ((m + n) % 2 == 1) {
            return a;
        }
        int b = max(low - 1 < 0 ? INT_MIN : nums2[low - 1], c - low - 1 < 0 ? INT_MIN : nums1[c - low - 1]);
        return (a + b) / 2.0;
    }
};