from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this can be used to avoid setting up a specific set for each row, col and box

        # rows = collections.defaultdict(set)
        # cols = collections.defaultdict(set)
        # boxes = collections.defaultdict(set)

        # creating hashmap to store the set of row, col and boxes number count
        rows = {}
        cols = {}
        boxes = {}

        for i in range(9):
            # creating a new set for each row
            rows[i] = set()
            for j in range(9):
                # grabbing current value
                current_val = board[i][j]

                # if it's a empty square move to the next value
                if current_val == ".":
                    continue

                # creating new set for column and 3 x 3 boxes if it hasn't been created already
                if j not in cols:
                    cols[j] = set()
                if (i // 3, j // 3) not in boxes:
                    boxes[i // 3, j // 3] = set()

                # checking if the current value has appeared in any of these sets, and if it hasn't we add them to the sets
                if current_val not in rows[i] and current_val not in cols[j] and current_val not in boxes[
                    (i // 3, j // 3)]:
                    rows[i].add(current_val)
                    cols[j].add(current_val)
                    boxes[i // 3, j // 3].add(current_val)
                else:
                    # return False if it has
                    return False

        return True
