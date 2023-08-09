

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]
# Output: 2


# We have n number and we know that (n+1)'th number is missing.
# Create array of length - n + 1.
# Iterate the given array "nums" and for each x in "nums" place 1 in new array in x'th position.
# In the end itterate through new array and if see 0 in some position return this index.
def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        exist = [0] * (n+1)
        # Mark all number that in range
        for x in nums:
            exist[x] = 1

        # Finde missing number
        for x in range(n+1):
            if exist[x] == 0:
                return x


if __name__ == "__main__":
    nums = [3,0,1]
    print(missingNumber(nums))
    nums = [0,1]
    print(missingNumber(nums))
    nums = [9,6,4,2,3,5,7,0,1]
    print(missingNumber(nums))


