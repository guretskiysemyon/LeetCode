'''
Author: Semyon Guretskiy
'''

'''


3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Solution:
    The solution uses the sliding window technique with a hashmap to track character positions:
    
    1. Window Management:
       - Left pointer marks start of current valid substring
       - Right pointer (i) explores new characters
       - Window contains current substring without repeating characters
    
    2. Character Tracking:
       - Hashmap stores the most recent position of each character
       - When duplicate found, move left pointer past the previous occurrence + 1
    
    3. Length Calculation:
       - Current window length = right - left + 1
       - Keep track of maximum window length seen
    
    Time Complexity: O(n) where n is length of string
    Space Complexity: O(min(m,n)) where m is size of character set
'''

def lengthOfLongestSubstring(s: str) -> int:
    # Dictionary to store the last position of each character
    char_position = {}
    
    # Handle empty and single character strings
    n = len(s)
    if n <= 1:
        return n
    
    # Initialize window start and max length
    left = 0           # Start of current window
    max_length = 0     # Length of longest valid substring found
    
    # Iterate through string (right pointer of window)
    for right in range(n):
        # If character seen and its last position is in current window
        if s[right] in char_position and char_position[s[right]] >= left:
            # Move left pointer past the previous occurrence
            left = char_position[s[right]] + 1
            
        # Update character's last seen position
        char_position[s[right]] = right
        
        # Update max_length if current window is larger
        current_length = right - left + 1
        if max_length < current_length:
            max_length = current_length
    
    return max_length

if __name__ == "__main__":
    # Test case 1: Multiple repeating characters
    s = "abcabcbb"
    # Expected output: 3 ("abc")
    result = lengthOfLongestSubstring(s)
    print(result)
    
    # Test case 2: No repeating characters
    s = "ab"
    # Expected output: 2 ("ab")
    result = lengthOfLongestSubstring(s)
    print(result)