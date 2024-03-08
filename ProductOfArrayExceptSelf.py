from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # postfix and prefix ordering
        output = [0] * len(nums)
        prefix = 1
        postfix = 1

        # calculate all of the prefix first
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        # then calculate all of the postfix
        for i in reversed(range(len(nums))):
            output[i] *= postfix
            postfix *= nums[i]

        #     prefix:
        # |       a       |   a*b   | a*b*c | a*b*c*d |

        #     postfix:
        # | a*b*c*d | b*c*d |   c*d   |      d        |

        #     the result is a multiply without the symbol in own position (the left value from prefix and the right one from postfix):
        # |    b*c*d  | a*c*d | a*b*d |   a*b*c   |

        return output
