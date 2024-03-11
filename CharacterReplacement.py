class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # map for the highest character count
        count = {}
        length = 0
        left = 0

        for r in range(len(s)):
            # creating first counts in map
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1

            # substring sliding window length
            window_length = r - left + 1

            # checking if there are more than k different characters
            if (window_length - max(count.values()) > k):
                # if there are, moving our sliding window to the right
                count[s[left]] -= 1
                left += 1

            length = max(length, r - left + 1)

        return length
