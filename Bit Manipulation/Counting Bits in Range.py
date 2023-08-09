

# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
# ans[i] is the number of 1's in the binary representation of i.
# Input: n = 2
# Output: [0,1,1]
# https://leetcode.com/problems/counting-bits/

# Explanation:
# 0 --> 0 --> 0
# 1 --> 1 --> 1
# 2 --> 10 --> 1
# 3 --> 11 --> 2
# 4 --> 100 --> 1
# 5 --> 101 --> 2
# 6 --> 110 --> 2
# 7 --> 111 --> 3
# In this example, we ca see that ans[2] = ans[0] + 1 and for ans[3] = ans[1] + 1 and so on.
#For general case let i be the power of 2 than for all 0 <= j <= i - 1 we have ans[i + j] = ans[j] + 1

def countBits(n):
        """
        :type n: int
        :rtype: List[int]
        """

        #Check the recursion basis.
        arr = [0] * (n + 1)
        if n >= 0:
            arr[0] = 0
        if n >= 1:
            arr[1] = 1

        i = 2
        k = 2
        while k <= n:
            j = 0
            # for all next i numbers we'll write ans[i+j]= ans[j] + 1.
            while j < i and k <= n:
                arr[k] = arr[j] + 1
                j += 1
                k += 1
            # Move to next power of 2.
            i *= 2
        return arr


if __name__ == "__main__":
    n = 2

    n = 5