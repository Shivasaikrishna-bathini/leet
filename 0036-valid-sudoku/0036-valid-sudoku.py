from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                row = (val, r)
                col = (c, val)
                box = (r // 3, c // 3, val)

                if row in seen or col in seen or box in seen:
                    return False

                seen.add(row)
                seen.add(col)
                seen.add(box)

        return True