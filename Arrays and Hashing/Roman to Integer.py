'''
Author: Semyon Guretskiy
'''

'''
13. Roman to Integer
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Link: https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150


Solution:
    Uses two-pointer sliding window approach:
    1. Compare current symbol with next symbol
    2. If next is larger, it's a subtraction case
    3. Otherwise, add current symbol value
    
    Time Complexity: O(n)
    Space Complexity: O(1)
'''

def romanToInt(s: str) -> int:
    # Map roman symbols to integer values  
    mapping = { 
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    n = len(s)
    result = 0
    i = 0
    
    # Process pairs of symbols
    while i < n - 1:
        # Check if subtraction case
        if mapping[s[i+1]] > mapping[s[i]]:
            # Add difference of next and current
            result += mapping[s[i+1]] - mapping[s[i]]
            i += 2
        else:
            # Add current symbol value
            result += mapping[s[i]]
            i += 1

    # Handle last symbol if needed
    if i == n-1:
        return result + mapping[s[i]]
    
    return result



if __name__ == "__main__":
    # Test cases
    test_cases = [
        "III",      # Simple addition
        "LVIII",    # Multiple symbols
        "MCMXCIV"   # Multiple subtraction cases
    ]
    
    for s in test_cases:
        print(f"Roman: {s}")
        print(f"Integer: {romanToInt(s)}\n")