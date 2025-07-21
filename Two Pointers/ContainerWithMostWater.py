# Container With Most Water

# You are given an integer array heights where heights[i] represents the height of the ithith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.
# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36

# Example 2:

# Input: height = [2,2,2]

# Output: 4

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            curHeight = min(heights[left], heights[right])
            width = right - left
            area = curHeight * width
            result = max(result, area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return result
    