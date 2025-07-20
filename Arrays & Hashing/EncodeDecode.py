# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]

# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word
        return result
    
    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            start = j + 1
            result.append(s[start:start + length])
            i = start + length
        return result