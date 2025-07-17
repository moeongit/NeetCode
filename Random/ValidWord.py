# A word is considered valid if:

#     It contains a minimum of 3 characters.
#     It contains only digits (0-9), and English letters (uppercase and lowercase).
#     It includes at least one vowel.
#     It includes at least one consonant.

# You are given a string word.

# Return true if word is valid, otherwise, return false.

# Notes:

#     'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
#     A consonant is an English letter that is not a vowel.


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
    
    hasvowel = False
    hascons = False

    for char in word:
        if char.isalpha():
            if char.lower() in "aeiou":
                hasvowel = True
            
            else:
                hascons = True
        
        elif not char.isdgigit():
            return False
    
    return hascons and hasvowel