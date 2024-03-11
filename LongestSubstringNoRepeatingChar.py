class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        # 2 pointer approach
        for i in range(len(s)):
            r = i + 1
            tmp_len = 0
            visited = set()
            if s[i] not in visited:
                tmp_len += 1
                visited.add(s[i])
                while r < len(s) and s[r] not in visited:
                    visited.add(s[r])
                    tmp_len += 1
                    r += 1
            else:
                continue

            length = max(length, tmp_len)

        return length