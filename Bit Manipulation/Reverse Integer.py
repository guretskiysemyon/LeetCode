
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


# Create a sting of this number. Reverse the string and cast to integer again.
def reverseByString(x:int) -> int:
    MAX = 2147483647  # 10
    MIN = -2147483648
    s_x = str(x) [::-1]
    if s_x[-1] == '-':
        rev = - int(s_x[:-1])
    else:
        rev = int(s_x)

    if rev > MAX or rev < MIN:
        return 0
    return rev

# Iterate from left to right. Take left digit add to reverse number and multiply by 10 to shift it. 
# Stop when x is 0.
# Example: 123 
# first: reverse = 3 and x = 12
# second: reverse = 32 and x = 1
# third: reverse = 321 and x = 0  
def reverse(x: int) -> int:
    MAX = 2147483647  # 10
    MIN = -2147483648
    
    # Modulu 10 doesn't work on negative numbers so use absolute value of number.
    minus = 0
    if x < 0:
        minus = 1
        x = - x
    
    # Main part of the algotirhm.
    inverse = 0
    while x != 0:
        inverse *= 10
        inverse += x % 10
        x = x//10

    # Return sign of x
    if minus:
        inverse = - inverse

    if inverse > MAX or inverse < MIN:
        inverse = 0
    
    return inverse



if __name__ == "__main__":

    MAX = 2147483647  # 10
    MIN = -2147483648
    rev = 0
    # Check all numbers in range
    for i in range(MIN, MAX+1):
        s_i = str(i)[::-1]
        try:
            if s_i[-1] == "-":
                rev = - int(s_i[:-1])
            else:
                rev = int(s_i)
        except:
            print(i)

        if rev > MAX or rev < MIN:
            rev = 0
        if rev != reverse(i):
            print(i)
        
    