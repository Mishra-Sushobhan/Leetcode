int mySqrt(int x) {
    if (x == 0) return 0;
    
    int left = 1, right = x;
    int result = 0;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;  // avoid overflow when computing mid
        
        // Check if mid * mid <= x, but avoid overflow by using division instead of multiplication
        if (mid <= x / mid) {
            // mid*mid <= x (safe check via division)
            result = mid;      // mid is a candidate answer, keep searching right for a larger one
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return result;
}