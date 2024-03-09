from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # start ptr and end ptr
        ptr1 = 0
        ptr2 = len(numbers) - 1

        # since the array is sorted, if the sum is too large, we can decrease the second ptr and try a lower value
        while ptr1 != ptr2:
            if numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1
            # same thing if the sum is too small, we can increase the first ptr and try a larger value
            elif numbers[ptr1] + numbers[ptr2] < target:
                ptr1 += 1
            elif numbers[ptr1] + numbers[ptr2] == target:
                return [ptr1 + 1, ptr2 + 1]