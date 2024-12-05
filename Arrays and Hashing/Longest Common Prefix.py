
'''
Semyon Guretskiy
'''

'''
14. Longest Common Prefix
Easy
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Link: https://leetcode.com/problems/longest-common-prefix/description/

Solution:
    Uses vertical scanning approach:
    1. Find length of shortest string
    2. Compare characters at same position across all strings
    3. Build prefix until mismatch found
    
    Time Complexity: O(S) where S is sum of all characters in all strings
    Space Complexity: O(1)
'''

def longestCommonPrefix(strs: list[str]) -> str:
    # Handle empty input or empty string in array
    if not strs or "" in strs:
        return ""
        
    # Find shortest string length
    min_length = min(len(s) for s in strs)
    prefix = ""
    
    # Check each position across all strings
    for i in range(min_length):
        current_char = strs[0][i]
        # Compare with same position in all other strings
        for s in strs:
            if s[i] != current_char:
                return prefix
        prefix += current_char
            
    return prefix

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ["flower","flow","flight"],     # Common prefix "fl"
        ["dog","racecar","car"],        # No common prefix
        ["","b"]                        # Empty string in array
    ]
    
    for strs in test_cases:
        print(f"Strings: {strs}")
        print(f"Common prefix: {longestCommonPrefix(strs)}\n")