class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int pos = m + n - 1;
        m--;
        n--;
        while (n >= 0) {
            if (m < 0 || nums2[n] > nums1[m]) {
                nums1[pos] = nums2[n--];
            } else {
                nums1[pos] = nums1[m--];
            }
            pos--;
        }
    }
};