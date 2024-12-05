

'''
Author: Semyon Gurestkiy
'''

'''
58. Length of Last Word
Easy

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Link: https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

Solution:
    Uses two pointers to find and measure last word:
    1. Skip trailing spaces from end
    2. Calculate length between next spaces
    
    Time Complexity: O(n)
    Space Complexity: O(1)
'''

def lengthOfLastWord(s: str) -> int:
    length = 0
    curr = len(s) - 1
    
    # Skip trailing spaces
    while curr >= 0 and s[curr] == " ":
        curr -= 1
        
    # Count word characters
    while curr >= 0 and s[curr] != " ":
        length += 1
        curr -= 1
        
    return length

            




strs = ["Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
        " ",
        "",
        "aa",
        "a",
        "          aa"
        ]


for s in strs:
    print(lengthOfLastWord(s))