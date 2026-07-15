int myAtoi(char* s) {
    int i = 0;
    int n = 0;
    while (s[n] != '\0') n++;  // length (optional, we can just check '\0')

    // Step 1: skip leading whitespace
    while (s[i] == ' ') i++;

    // Step 2: determine sign
    int sign = 1;
    if (s[i] == '+' || s[i] == '-') {
        if (s[i] == '-') sign = -1;
        i++;
    }

    // Step 3: read digits, building result while checking overflow as we go
    int result = 0;
    const int INT_MAX_ = 2147483647;
    const int INT_MIN_DIV10 = -214748364; // INT_MIN / 10, since INT_MIN = -2147483648
    // We'll build using negative accumulation to naturally handle INT_MIN case,
    // then apply sign at the end carefully.

    while (s[i] >= '0' && s[i] <= '9') {
        int digit = s[i] - '0';

        // Check overflow before result = result * 10 + digit
        if (result > INT_MAX_ / 10 || (result == INT_MAX_ / 10 && digit > 7)) {
            return (sign == 1) ? INT_MAX_ : (-INT_MAX_ - 1);
        }

        result = result * 10 + digit;
        i++;
    }

    return sign * result;
}