# Valid Anagram
# Solved
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i in s:
            if i not in hash1:
                hash1[i] = 1
            hash1[i] += 1
        
        for i in t:
            if i not in hash2:
                hash2[i] = 1
            hash2[i] += 1
        
        return hash1 == hash2
