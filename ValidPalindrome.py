class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower()

        for c in new_s:
            if not c.isalnum():
                new_s = new_s.replace(c, "")

        return new_s == new_s[::-1]
        #
        # if len(new_s) == 0:
        #     return True
        #
        # end = len(new_s) - 1
        #
        # for i in range(0, len(new_s)):
        #     if (new_s[i] != new_s[end]):
        #         return False
        #     end -= 1
        #
        # return True


