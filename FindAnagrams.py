from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        # comparing hashmaps to each other
        sCount = {}
        pCount = {}
        index = []

        # looping through and adding first 3 characters to each map
        for i in range(len(p)):
            if s[i] not in sCount:
                sCount[s[i]] = 1
            else:
                sCount[s[i]] += 1

            if p[i] not in pCount:
                pCount[p[i]] = 1
            else:
                pCount[p[i]] += 1

        # if first three are the same, then we can add index 0 to list
        if pCount == sCount:
            index.append(0)

        # left pointer
        left = 0

        # looping from where we left off
        for i in range(len(p), len(s)):
            # getting next character and adding to map
            if s[i] in sCount:
                sCount[s[i]] += 1
            else:
                sCount[s[i]] = 1

            # getting rid of leftmost character since we are moving the sliding window
            sCount[s[left]] -= 1

            # removing from map to do equality check properly
            if sCount[s[left]] == 0:
                sCount.pop(s[left])

            # incrementing left counter to keep sliding window at 3
            left += 1

            # checking if map count for both are the same
            if sCount == pCount:
                index.append(left)

        return index
