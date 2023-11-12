from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            value = nums[mid]
            if mid < len(nums) - 1 and value < nums[mid + 1]:
                low = mid + 1
            elif mid > 0 and value < nums[mid - 1]:
                high = mid - 1
            else:
                return mid