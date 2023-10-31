class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numbers:
                return [numbers[complement], i]
            numbers[nums[i]] = i

        return []