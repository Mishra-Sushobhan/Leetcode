char* addBinary(char* a, char* b) {
    int lenA = strlen(a);
    int lenB = strlen(b);
    int maxLen = (lenA > lenB) ? lenA : lenB;
    
    // Result can have at most maxLen + 1 digits, plus null terminator
    char* result = (char*)malloc(maxLen + 2);
    result[maxLen + 1] = '\0';
    
    int i = lenA - 1;   // pointer into a, from the right
    int j = lenB - 1;   // pointer into b, from the right
    int k = maxLen;     // pointer into result, from the right
    int carry = 0;
    
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) {
            sum += a[i] - '0';
            i--;
        }
        if (j >= 0) {
            sum += b[j] - '0';
            j--;
        }
        result[k] = (sum % 2) + '0';
        carry = sum / 2;
        k--;
    }
    
    // If we didn't fill the leftmost slot (i.e., no final carry produced a leading '1'),
    // shift the string to remove the unused leading position.
    char* finalResult = result + (k + 1);
    
    // Make a clean copy so the caller can free() at the exact returned pointer if desired
    char* output = strdup(finalResult);
    free(result);
    return output;
}