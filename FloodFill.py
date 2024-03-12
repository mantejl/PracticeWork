from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # getting current color and getting the bounds for the matrix
        cur_color = image[sr][sc]
        height = len(image)
        width = len(image[0])

        def fill(sr, sc):
            # if the current cell is valid and is the same color as our starting cell and has not been visited
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == cur_color and image[sr][sc] != color:
                # change the color for it
                image[sr][sc] = color
                # and call the same check for all the surrounding cells
                fill(sr + 1, sc)
                fill(sr - 1, sc)
                fill(sr, sc + 1)
                fill(sr, sc - 1)

        # call the function
        fill(sr, sc)

        return image