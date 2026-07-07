class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes (the '-' sign breaks symmetry)
        # Numbers ending in 0 (except 0 itself) can't be palindromes either,
        # since a palindrome can't start with 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        # For even-length numbers, x == reverted at the end
        # For odd-length numbers, the middle digit is irrelevant, so we drop it with reverted // 10
        return x == reverted or x == reverted // 10