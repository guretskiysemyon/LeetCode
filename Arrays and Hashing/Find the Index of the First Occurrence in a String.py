'''
Author: Semyon Guretskiy
'''


'''
28. Find the Index of the First Occurrence in a String
Easy

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string?envType=study-plan-v2&envId=top-interview-150

Solution:
    Uses Knuth-Morris-Pratt (KMP) algorithm:
    1. Build failure function for pattern (needle)
    2. Use failure function to skip unnecessary comparisons
    3. Match pattern against text in single pass
    
    Time Complexity: O(n + m) where n is length of haystack, m is length of needle
    Space Complexity: O(m) for failure function array
'''

def strStr(haystack: str, needle: str) -> int:
    def compute_f(pattern):
        # Compute failure function for KMP algorithm
        n = len(pattern)
        f = [0]  # First position always 0
        
        for i in range(1, n):
            # Start with previous position's value
            k = f[i - 1]
            
            # Keep going back until match found or beginning reached
            while k != 0 and pattern[i] != pattern[k]:
                k = f[k - 1]

            # Extend match if possible
            if pattern[i] == pattern[k]:
                k += 1

            f.append(k)
        return f
    
    # Get failure function for pattern
    f = compute_f(needle)
    n = len(haystack)
    m = len(needle)

    # Position in pattern
    p = 0

    # Match pattern against text
    for i in range(n):
        # Use failure function to skip invalid matches
        while p != 0 and haystack[i] != needle[p]:
            p = f[p-1]
        
        # Extend match if possible
        if haystack[i] == needle[p]:
            p += 1
        
        # Full pattern matched
        if p == m:
            return i + 1 - m

    return -1

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("sadbutsad", "sad"),   # Pattern at start
        ("leetcode", "leeto")   # Pattern not found
    ]
    
    for haystack, needle in test_cases:
        print(f"Text: {haystack}")
        print(f"Pattern: {needle}")
        print(f"First occurrence at: {strStr(haystack, needle)}\n")