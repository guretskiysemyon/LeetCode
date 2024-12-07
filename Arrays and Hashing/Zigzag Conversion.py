'''
Author: Semyon Guretskiy
'''

'''
6. Zigzag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Constraints:
   - 1 <= s.length <= 1000
   - s consists of English letters (lower-case and upper-case), ',' and '.'.
   - 1 <= numRows <= 1000

Link: https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150

Solution:
The problem can be solved in two ways:

1. Using Array Traversal (First Solution):
  - Create array of strings for each row
  - Traverse input string and add characters to appropriate rows
  - Use boolean flag to track direction (down/up)
  - Time Complexity: O(n) where n is length of input string
  - Space Complexity: O(n) to store result strings

2. Using Pattern Finding (Second Solution):
  - For each level, calculate steps between characters that belong to that level
  - First and last rows have constant step size, middle rows alternate between two steps
  - Time Complexity: O(n)
  - Space Complexity: O(n) for result string

'''

def convert(s: str, numRows: int) -> str:
   # Handle edge case of single row
   if numRows == 1:
       return s
       
   # Create array of strings for each row
   rows = [""] * numRows
   
   # Current row index and direction flag
   i = 0
   down = True

   # Iterate through each character
   for c in s:
       # Add character to current row
       rows[i] += (c)
       
       # Change direction at boundaries
       if i == numRows - 1 and down:
           down = False
       elif i == 0 and not down:
           down = True
       
       # Move to next row based on direction
       if down:
           i += 1
       else:
           i -= 1
   
   # Join all rows together
   return "".join(rows)


def convert(s: str, numRows: int) -> str:
   # Handle edge case of single row
   if numRows == 1:
       return s
  
   result = ""
   # Calculate maximum step between same pattern elements
   max_step = (numRows - 1) * 2
   
   # Process each level/row
   level = 0
   while level < numRows:
       # Calculate steps for current level
       first_step = max_step - level * 2  # Step to next char in same pattern
       second_step = max_step - first_step # Step to char in next pattern
       
       # Process all chars in current level
       i = 0
       while level + i < len(s):
           # Add current char to result
           result += s[level + i]
           
           # Calculate next position using alternating steps
           if i % max_step == 0 and first_step != 0:
               i += first_step
           else:
               i += second_step
       level += 1
   
   return result




# Test cases        
s = "PAYPALISHIRING"
rows = 3
res = convert(s, rows)
print(res)  # Expected: "PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
rows = 4
res = convert(s, rows)
print(res)  # Expected: "PINALSIGYAHRPI"

s = "A"
rows = 1
res = convert(s, rows)
print(res)  # Expected: "A"

s ="ABC"
rows = 2
res = convert(s, rows)
print(res)  # Expected: "ACB"