class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # current pointer that is our break statement and checks if it hasn't
        # gone over the length of the string
        curr = 0
        final_str = ""
        while curr < len(s):
            # end pointer is the kth value from curr that we are testing
            end = curr + k
            temp_str = s[curr:end]
            new_str = temp_str[::-1]
            final_str += new_str
            # getting the remaining characters from the string set
            final_str += s[end:curr + 2 * k]
            curr += 2 * k

        return final_str

        # old implementation, doesn't pass all test cases

        # end = 2 * k
        # curr = 0
        # final_str = ""
        # while s[curr:end]:
        #     if len(s[curr:end]) < k:
        #         temp_str = s[curr:end]
        #         new_str = temp_str[::-1]
        #         final_str += new_str
        #         break
        #     else:
        #         print("current set string", s[curr:end])
        #         temp_str = s[curr:curr+k]
        #         print("current string", temp_str)
        #         new_str = temp_str[::-1]
        #         print("reversed string", new_str)
        #         combined_str = new_str + s[curr+k:end]
        #         print("combined string", combined_str)
        #         final_str += combined_str
        #         curr = end
        #         end *= 2

        # return final_str
