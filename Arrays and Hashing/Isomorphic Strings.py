'''
Author: Semyon Guretkiy
'''

'''
205. Isomorphic Strings
Easy
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Link: https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150

Constraints:

- 1 <= s.length <= 5 * 104
- t.length == s.length
- s and t consist of any valid ascii character.

Solution:
Solution:
The problem can be solved by tracking two things:
1. Mapping from characters in s to characters in t
2. Which characters in t are already used in mappings

We iterate through both strings simultaneously and for each position check:
1. If the current character in s is already mapped:
   - Verify that its mapping matches the current character in t
2. If the character is not mapped:
   - Check if the current character in t is not already mapped to another character
3. If neither check fails:
   - Create new mapping and continue

This ensures that:
- Each character maps to only one other character
- No two characters map to the same character
- The order of characters is preserved
We use dictionary for character mappings and another dictionary as a set to track used characters.


Time Complexity: O(n) in average where n is length of input strings
Space Complexity: O(k) where k is size of character set
'''

def isIsomorphic(s: str, t: str) -> bool:
   # Dictionary to store character mappings from s to t
   s_to_t_map = {}
   # Dictionary used as a set to track which characters in t are already mapped
   used = {}
   
   # Iterate through both strings simultaneously
   for c_s, c_t in zip(s, t):
       # If character from s is already mapped
       if c_s in s_to_t_map:
           # Check if current mapping matches
           if s_to_t_map[c_s] != c_t:
               return False
       # If character from s is not mapped but t's character is already used
       elif c_t in used:
           return False
       # Create new mapping and mark t's character as used    
       s_to_t_map[c_s] = c_t
       used[c_t] = True
   return True

# Test cases
tests = ["egg",
       "add",
       "foo",
       "bar",
       "paper",
       "title",
       "bbbaaaba",
       "aaabbbba"
       ]

# Run tests in pairs
for i in range(0, len(tests)- 1, 2):
   print(f"{i} {i+1}")
   print(tests[i],tests[i+1])
   print(isIsomorphic(tests[i],tests[i+1]))