from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list to make the problem easier and use two pointer approach
        new_list = sorted(nums)
        result = []

        # loop
        for i in range(len(nums)):
            # checking if previous value not being rechecked
            if i > 0 and new_list[i] == new_list[i - 1]:
                continue

            # two sum part 2 (two pointer approach)
            start = i + 1
            end = len(nums) - 1

            # while the starting pointer is less than the ending pointer
            while start < end:
                # calculate the total sum
                total_sum = new_list[i] + new_list[start] + new_list[end]
                # two sum 2 approach where we continue to cut down depending on value of sum
                if total_sum > 0:
                    end -= 1
                elif total_sum < 0:
                    start += 1
                # if sum is 0 then we add to list and decrease the right pointer (can also increase left ptr)
                else:
                    result.append([new_list[i], new_list[start], new_list[end]])
                    end -= 1
                    # making sure we are not checking the same two values again, so skipping that value to test new values
                    while start < end and new_list[end] == new_list[end + 1]:
                        end -= 1

        return result