from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force approach
        # nested for loop that searches through entire list and checks all possible
        # combinations to see which two numbers add up to target

        # optimized approach would be to loop through list and have map of nums and
        # their respective indexes
        nums_index = {}
        for i in range(len(nums)):
            nums_index[nums[i]] = i

        print(nums_index.keys())

        # loop through the list and subtract current number from target and check
        # if complement exists in map

        for i in range(len(nums) - 1):
            comp = target - nums[i]
            if comp in nums_index.keys() and i != nums_index[comp]:
                return [i, nums_index[comp]]