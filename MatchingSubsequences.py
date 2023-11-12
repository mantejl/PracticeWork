from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0

        def isSub(string):
            i = -1
            for c in string:
                i = s.find(c, i + 1)
                if i == -1:
                    return False
            return True

        for w in words:
            if isSub(w):
                count += 1

        return count