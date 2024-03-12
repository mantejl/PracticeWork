from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # row and col arrays
        n = 3
        row = [0] * n
        col = [0] * n
        #
        diag1 = 0
        diag2 = 0
        player = 1

        for r, c in moves:
            row[r] += player
            col[c] += player
            if r == c:
                diag1 += player
            if r + c == n - 1:
                diag2 += player
            if abs(row[r]) == 3 or abs(col[c]) == 3 or abs(diag1) == 3 or abs(diag2) == 3:
                if player == 1:
                    return "A"
                else:
                    return "B"
            player *= -1
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
