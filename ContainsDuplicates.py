class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set has O(1) lookup time while list has O(n) lookup time

        # count = {}

        # for n in nums:
        #     if n in count.keys():
        #         count[n] += 1
        #     else:
        #         count[n] = 1

        # for val in count.values():
        #     if val != 1:
        #         return True

        # return False

        num_appears = set()

        for n in nums:
            if n in num_appears:
                return True
            num_appears.add(n)

        return False