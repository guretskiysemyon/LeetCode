'''
Author: Semyon Guretskiy
'''

'''
383. Ransom Note
Easy
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Link: https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

Solution:
This problem can be solved in two ways:

1. Dictionary/Hash Map Approach (Optimal Solution):
   - Create a dictionary to count frequency of characters in magazine
   - Iterate through ransomNote and check if we have enough characters
   - Time Complexity: O(m + n) in average where m is length of magazine and n is length of ransomNote
   - Space Complexity: O(k) where k is number of unique characters in magazine
   
2. String Manipulation Approach:
   - Iterate through ransomNote characters
   - For each character, check if it exists in magazine and remove first occurrence
   - Time Complexity: O(n * m)
   - Space Complexity: O(1)

'''

def canConstruct(ransomNote: str, magazine: str) -> bool:
    # Create a dictionary to store character frequencies from magazine
    magazine_dict = {}

    # Count frequency of each character in magazine
    for c in magazine:
        if c in magazine_dict:
            magazine_dict[c] += 1
        else:
            magazine_dict[c] = 1
    
    # Check if we can construct ransomNote
    for c in ransomNote:
        # If character not in magazine, we can't construct the note
        if c not in magazine_dict:
            return False
        
        # Decrease the frequency of used character
        magazine_dict[c] -= 1
        # If we've used all instances of this character, remove it
        if magazine_dict[c] == 0:
            magazine_dict.pop(c)
    
    return True


def canConstruct(ransomNote: str, magazine: str) -> bool:
    # Iterate through each character in ransomNote
    for c in ransomNote:
        # If character not in magazine, we can't construct the note
        if c not in magazine:
            return False
        else:
            # Remove the first occurrence of the character from magazine
            magazine = magazine.replace(c, '', 1)
    return True


# More efficient Pythonic solution using Counter
from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    # Create frequency counters for both strings
    magazine_counter = Counter(magazine)
    ransom_counter = Counter(ransomNote)
    
    # Check if magazine has enough of each character
    return all(ransom_counter[c] <= magazine_counter[c] for c in ransom_counter)


# Test cases
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))

ransomNote = "aa"
magazine = "ab"
print(canConstruct(ransomNote, magazine))