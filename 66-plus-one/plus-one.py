class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Go from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # no carry needed, we're done
            digits[i] = 0  # digit was 9, becomes 0, carry propagates left

        # If we get here, every digit was 9 (e.g. 999 -> 1000)
        # All digits are now 0, so prepend a 1
        return [1] + digits