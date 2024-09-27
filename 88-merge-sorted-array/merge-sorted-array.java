class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        // Initialize pointers
        int i = m - 1; // Pointer to the last element in nums1's valid range
        int j = n - 1; // Pointer to the last element in nums2
        int k = m + n - 1; // Pointer to the last position in nums1's total length

        // Merge nums1 and nums2 from the end
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k] = nums1[i]; // Take element from nums1
                i--;
            } else {
                nums1[k] = nums2[j]; // Take element from nums2
                j--;
            }
            k--; // Move the insertion pointer
        }
    }
}