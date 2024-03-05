class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        s_dict = {}
        t_dict = {}

        for i in range(s_len):
            if s[i] in s_dict.keys():
                s_dict[s[i]] += 1
            elif s[i] not in s_dict.keys():
                s_dict[s[i]] = 1

            if t[i] in t_dict.keys():
                t_dict[t[i]] += 1
            elif t[i] not in t_dict.keys():
                t_dict[t[i]] = 1

        for i in range(t_len):
            if t[i] not in s_dict.keys() or s_dict[t[i]] != t_dict[t[i]]:
                return False

        return True
