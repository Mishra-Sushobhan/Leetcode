class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip trailing spaces first, then find the last space before the last word
        s = s.rstrip()
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
        