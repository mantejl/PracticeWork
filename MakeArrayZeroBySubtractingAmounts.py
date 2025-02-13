from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # operations = 0 
        # n_nums = sorted(nums)

        # for n in range(len(n_nums)): 
        #     number = n_nums[n]
        #     if n_nums[n] == 0:
        #         continue 
        #     else:
        #         for i in range(n, len(n_nums)): 
        #             n_nums[i] -= number
        #         operations += 1

        # return operations

        numbers = set()

        for n in nums:
            if n != 0 and n not in numbers:
                numbers.add(n)
        
        return len(numbers)