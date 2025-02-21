# Group Anagrams
# Solved

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]

# Example 3:

# Input: strs = [""]

# Output: [[""]]

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            sortedWord = str(sorted(i))
            if sortedWord not in hashMap:
                hashMap[sortedWord] = []
            hashMap[sortedWord].append(i)
        
        return list(hashMap.values())