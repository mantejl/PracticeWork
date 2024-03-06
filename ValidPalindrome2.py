class Solution:
    def validPalindrome(self, s: str) -> bool:
        # original way: create two separate strings if initial not equal, then run palindrome test on that

        # end = len(s) - 1
        # new_s1 = ""
        # new_s2 = ""
        # initial_check = True

        # for i in range(len(s)):
        #     if s[end] != s[i]:
        #         new_s1 = s[:i] + s[i+1:]
        #         new_s2 = s[:end] + s[end+1:]
        #         initial_check = False
        #         break
        #     end -= 1

        # if initial_check:
        #     return True

        # end1 = len(new_s1) - 1
        # end2 = len(new_s2) - 1
        # checkOne = True
        # checkTwo = True

        # for i in range(len(new_s1)):
        #     if new_s1[i] != new_s1[end1]:
        #         checkOne = False
        #     if new_s2[i] != new_s2[end2]:
        #         checkTwo = False
        #     end1 -= 1
        #     end2 -= 1

        # if checkOne or checkTwo:
        #     return True
        # else:
        #     return False

        # while loop with pythonic code and 2 ptr approach

        end = len(s) - 1
        start = 0
        while (start <= end):
            if (s[start] != s[end]):
                s_one = s[:start] + s[start + 1:]
                s_two = s[:end] + s[end + 1:]
                return s_one == s_one[::-1] or s_two == s_two[::-1]
            start += 1
            end -= 1

        return True
