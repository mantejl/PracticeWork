from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorting the intervals based on their start values
        intervals.sort(key = lambda pair: pair[0])

        # to start our comparision we can set first value into output 
        output = [intervals[0]]

        # go through the rest of the intervals with the start and end value 
        for start, end in intervals[1:]: 
            # get the most recent end value
            mostRecentEnd = output[-1][1] 
            # if the start value is less than or equal to the most recent end value
            if start <= mostRecentEnd: 
                # update the most recent end value to the max of the most recent end value and the end value
                output[-1][1] = max(mostRecentEnd, end)
            else:
                # if the start value is greater than the most recent end value, then we can add the interval to the output
                output.append([start, end])
        
        return output