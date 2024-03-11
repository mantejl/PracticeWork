from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointer approach, start and end of list
        l = 0
        r = len(height) - 1
        area = 0
        # while loop
        while l < r:
            # getting the minimum height between the two points, since that's our deciding factor
            min_h = min(height[l], height[r])
            # getting the new area if it's bigger
            area = max(area, min_h * (r - l))
            # moving the pointers based on which one is smaller
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area