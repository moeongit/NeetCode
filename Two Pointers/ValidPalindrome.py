# Valid Palindrome
# Solved

# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true

# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            
            elif not s[right].isalnum():
                right -= 1
            
            elif s[left].lower() != s[right].lower():
                return False
            
            else:
                left += 1
                right -= 1

        return True