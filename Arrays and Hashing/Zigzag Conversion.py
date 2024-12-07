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
'''

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    rows = [""] * numRows
    
    i = 0
    down = True

    for c in s:
        rows[i] += (c)
        if i == numRows - 1 and down:
            down = False
        elif i == 0 and not down:
            down = True
        
        if down:
            i += 1
        else:
            i -= 1
    
    
    return "".join(rows)



def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
   
    result = ""
    max_step = (numRows - 1) * 2
    level = 0
    while level < numRows:
        first_step = max_step - level * 2
        second_step = max_step - first_step
        i = 0
        while level + i < len(s):
            result += s[level + i]
            if i % max_step == 0 and first_step != 0:
                i += first_step
            else:
                i += second_step
        level += 1
    
    return result
        
        
        
             


s = "PAYPALISHIRING"
rows = 3
res = convert(s, rows)
print(res)
s = "PAYPALISHIRING"
rows = 4
res = convert(s, rows)
print(res)
s = "A"
rows = 1
res = convert(s, rows)
print(res)

s ="ABC"
rows = 2
res = convert(s, rows)
print(res)


