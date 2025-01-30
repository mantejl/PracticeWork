from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i in range(0, len(nums)):
            index_map[nums[i]] = i
        
        for i in range(0, len(nums)): 
            comp = target - nums[i] 
            if comp in index_map.keys() and index_map[comp] != i:
                return [i, index_map[comp]]