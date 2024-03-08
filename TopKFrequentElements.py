from heapq import heappush, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # max heap implementation, runtime isn't optimized
        pq = []
        res = []

        for n in nums:
            count = nums.count(n)
            heappush(pq, (-count, n))

        i = 0
        while i < k:
            freq = heappop(pq)
            freq_num = freq[1]
            if freq_num not in res:
                res.append(freq_num)
                i += 1

        return res

        # creating hashmap and storing frequency for each characters
        freq = {}
        res = []

        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1

        # sorting dictionary and then reversing the list to get max to min
        # sorting freq.items() -> numbers by their frequency, which is f[1]
        sorted_freq = dict(sorted(freq.items(), key=lambda f: f[1]))
        val = list(sorted_freq.keys())
        reverse_val = val[::-1]

        # adding to result list
        for i in range(k):
            res.append(reverse_val[i])

        return (res)