from _ast import List
from heapq import heappush, heappop


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pq = []
        ranks = [None] * len(score)
        place = 0

        # max heap which has score and index of score in original list
        for i in range(0, len(score)):
            heappush(pq, (-score[i], i))

        # while the heap exists, we are popping and grabbing the index of the score in the original list
        while pq:
            athlete = heappop(pq)
            indx = athlete[1]
            # monitor the first three values of the heap to set them to correct
            if place == 0:
                ranks[indx] = "Gold Medal"
            elif place == 1:
                ranks[indx] = "Silver Medal"
            elif place == 2:
                ranks[indx] = "Bronze Medal"
            else:
                ranks[indx] = str(place + 1)

            # used to track what place we are on
            place += 1

        return ranks
