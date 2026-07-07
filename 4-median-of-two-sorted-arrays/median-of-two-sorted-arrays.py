class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array so binary search runs on the shorter one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2  # size of the "left half" combined

        while left <= right:
            i = (left + right) // 2   # partition point in nums1
            j = half - i               # partition point in nums2

            # Values around the partitions (use +/- infinity for out-of-bounds)
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')

            # Check if this partition is correct
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found the correct partition
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                # Too many elements from nums1 on the left, move partition left
                right = i - 1
            else:
                # Too few elements from nums1 on the left, move partition right
                left = i + 1
        