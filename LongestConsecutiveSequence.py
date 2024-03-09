from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use a set for quicker lookup
        nums_set = set(nums)
        longest_seq = 0

        # checking if current number is the start of our sequence
        for num in nums:
            # if it is, then we keep finding it's next biggest value and incrementing the counter
            if (num - 1) not in nums_set:
                tmp = num
                curr_seq = 0
                while tmp in nums_set:
                    curr_seq += 1
                    tmp += 1
                # taking the longest sequence and setting it
                longest_seq = max(longest_seq, curr_seq)

        return longest_seq
