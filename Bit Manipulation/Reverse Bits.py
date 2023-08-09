

# Reverse bits of a given 32 bits unsigned integer.
# https://leetcode.com/problems/reverse-bits/


def reverseBits(n):
        n = ((n & 0x0000FFFF) << 16) | ((n & 0xFFFF0000) >> 16)
        n = ((n & 0x00FF00FF) << 8) | ((n & 0xFF00FF00) >> 8)
        n = ((n & 0x0F0F0F0F) << 4) | ((n & 0xF0F0F0F0) >> 4)
        n = ((n & 0x33333333) << 2) | ((n & 0xCCCCCCCC) >> 2)
        n = ((n & 0x55555555) << 1) | ((n & 0xAAAAAAAA) >> 1)
       
        return n


if __name__ == "__main__":
    n = 0b00000010100101000001111010011100
    print(reverseBits(n))
    n = 0b11111111111111111111111111111101
    print(reverseBits(n))
    