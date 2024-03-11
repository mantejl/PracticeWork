from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            index = (l + r) // 2
            if nums[index] == target:
                return index
            elif target < nums[index]:
                r = index - 1
            elif target > nums[index]:
                l = index + 1

        return -1
