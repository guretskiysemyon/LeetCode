


# Write a function that takes the binary representation of an unsigned integer 
# and returns the number of '1' bits it has (also known as the Hamming weight).
# https://leetcode.com/problems/number-of-1-bits/



# The idea is just to count number of 1 bits in number
# by iteration ans using mask.
def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    counter = 0
    mask = 1    
    for j in range(32):
        # check if in j'th position is 1 and add 1 to counter is so.
        if mask & n != 0:
            counter += 1
        mask <<= 1
    return counter


if __name__== "__main__":
    n = 0b00000000000000000000000000001011
    print(hammingWeight(n))
    n = 0b00000000000000000000000010000000
    print(hammingWeight(n))
    n = 0b11111111111111111111111111111101
    print(hammingWeight(n))
