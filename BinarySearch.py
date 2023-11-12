from typing import List


def binary_search(nums: List[int], target: int):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high -= 1
        elif nums[mid] < target:
            low += 1
        else:
            return mid
    return -1

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))
print(binary_search([1,2,3,5,8], 2))
print(binary_search([1,2,3,5,8], 8))