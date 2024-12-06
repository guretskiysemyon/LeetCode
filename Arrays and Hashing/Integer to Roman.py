'''
Author: Semyon Guretskiy
'''
'''
12. Integer to Roman
Medium

Roman numerals use seven symbols with the following values:
Symbol  Value
I       1
V       5
X       10
L       50
C       100
D       500
M       1000

Rules for conversion:
1. Regular case: Use largest possible symbols (e.g., 3 = III)
2. Subtractive case: For 4 and 9, use subtraction (e.g., 4 = IV, 9 = IX)
3. Valid subtractive pairs: IV(4), IX(9), XL(40), XC(90), CD(400), CM(900)
4. No more than three consecutive same symbols allowed

Link: https://leetcode.com/problems/integer-to-roman/description/

Solution:
    Uses place value approach:
    1. Process number digit by digit starting from thousands
    2. Handle special cases (4,9) with subtractive notation
    3. Handle regular cases using standard symbols
    4. Build result string from left to right
    
    Space Complexity: O(1)
'''

def intToRoman(num: int) -> str:
    # Map values to Roman symbols
    mapping = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
     
    result = ""
    place_value = 1000  # Start with thousands
    
    while place_value != 0:
        # Get digit at current place value
        digit = num // place_value
        num = num % place_value  # Remove processed digit
        
        if digit == 4:
            # Subtractive case for 4
            result += mapping[place_value] + mapping[place_value * 5]
               
        elif digit == 9:
            # Subtractive case for 9
            result += mapping[place_value] + mapping[place_value * 10]
        
        else:
            # Regular case
            if digit >= 5:
                # Add five's symbol if needed
                result += mapping[place_value * 5]
                digit -= 5
            
            # Add remaining ones symbols
            result += mapping[place_value] * digit
        
        place_value //= 10  # Move to next place value
    
    return result

if __name__ == "__main__":
    test_cases = [
        564,   # Regular case
        1994,  # Multiple subtractive cases
        3749   # Mixed case
    ]
    
    for num in test_cases:
        print(f"Number: {num}")
        print(f"Roman: {intToRoman(num)}\n")