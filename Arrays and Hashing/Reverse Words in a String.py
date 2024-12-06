'''
Author: Semyon Guretskiy
'''

'''
151. Reverse Words in a String
Medium

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Link: https://leetcode.com/problems/reverse-words-in-a-string/description/

Solution:
    Three different approaches implemented:

    1. Built-in Functions:
       - Uses split() to tokenize words
       - Reverses list and joins with spaces
       - Most concise but doesn't show algorithmic thinking
       
    2.Implementation Without Built-in Functions:
       - Replicates the logic of the first approach but uses standard functions to implement it manually.
       - Focuses on showcasing the underlying logic without relying on Python's built-in capabilities.

    3. In-Place Reversal (O(1) Space):
       - Reverses the entire string first.
       - Then reverses each word individually.
       - Simultaneously removes extra spaces using pop().
'''

# Approach 1: Using Built-in Functions
def reverseWords1(s: str) -> str:
    return ' '.join(s.split()[::-1])

# Approach 2: My implementation of first aproach logic
def reverseWords2(s: str) -> str:
    # Add space to handle last word
    s += " "
    word = ""
    words = []
    
    # Build words character by character
    for c in s:
        if c == " ":
            if word:  # Only add non-empty words
                words.append(word)
                word = ""
            continue
        word += c
    
    # Build result string with reversed words
    result = ""
    for w in words[::-1]:
        result += f"{w} "
    
    return result[:-1]  # Remove trailing space

# Approach 3: In-place Reversal with Space Removal
def reverseWords3(s: str) -> str:
    def reverse(s: list, left: int, right: int):
        # Helper function to reverse portion of list
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    # Convert to list and reverse whole string
    s = list(s)
    reverse(s, 0, len(s) - 1)
    s.append(" ")  # Add space to handle last word

    # Remove leading spaces
    while s and s[0] == " ":
        s.pop(0)

    left = right = 0
    while right < len(s):
        # Find word boundary
        if s[right] != " ":
            right += 1
            continue

        # Reverse individual word
        reverse(s, left, right-1)
        
        # Move past the space
        right += 1
        # Remove extra spaces between words
        while right < len(s) and s[right] == " ":
            s.pop(right)
        
        # Setup for next word
        left = right
        right += 1
    
    # Remove final trailing space
    if s[-1] == " ":
        s.pop()
    
    return "".join(s)

if __name__ == "__main__":
    test_cases = [
        "the sky is blue",     # Normal case
        "  hello world  ",     # Leading/trailing spaces
        "a good   example"     # Multiple spaces between words
    ]
    
    for s in test_cases:
        print(f'Input: "{s}"')
        print(f'Output: "{reverseWords3(s)}"\n')

