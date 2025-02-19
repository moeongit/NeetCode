# Contains Duplicate

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true


# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false


from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()

        for i in nums:
            if i in hashMap:
                return True
            hashMap.add(i)
        return False