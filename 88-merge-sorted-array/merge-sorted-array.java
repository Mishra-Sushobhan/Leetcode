class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;        // pointer for last valid element in nums1
        int j = n - 1;        // pointer for last element in nums2
        int k = m + n - 1;    // pointer for last position in nums1 (write position)
        
        // Merge from the back, placing the larger element at the end
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
            } else {
                nums1[k] = nums2[j];
                j--;
            }
            k--;
        }
        
        // If there are remaining elements in nums2, copy them over
        // (remaining elements in nums1 are already in place, since they occupy the front)
        while (j >= 0) {
            nums1[k] = nums2[j];
            j--;
            k--;
        }
        
        // No need to handle remaining nums1 elements (if i >= 0 when j < 0):
        // they're already in their correct positions at the front of nums1.
    }
}