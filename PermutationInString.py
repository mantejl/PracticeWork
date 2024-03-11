class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # same thing as find all anagrams in string
        if len(s1) > len(s2):
            return False

        s_one = {}
        s_two = {}

        for i in range(len(s1)):
            if s1[i] in s_one:
                s_one[s1[i]] += 1
            else:
                s_one[s1[i]] = 1

            if s2[i] in s_two:
                s_two[s2[i]] += 1
            else:
                s_two[s2[i]] = 1

        if s_one == s_two:
            return True

        left = 0

        for i in range(len(s1), len(s2)):
            if s2[i] not in s_two:
                s_two[s2[i]] = 1
            else:
                s_two[s2[i]] += 1

            s_two[s2[left]] -= 1

            if s_two[s2[left]] == 0:
                s_two.pop(s2[left])

            left += 1

            if s_one == s_two:
                return True

        return False
