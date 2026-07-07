class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: with 1 row (or fewer rows than characters needed to zigzag),
        # the string is unchanged
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            # Reverse direction whenever we hit the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)