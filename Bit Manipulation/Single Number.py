



# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# https://leetcode.com/problems/single-number/


# The idea is to use xor. If there every number appears twice then xor operation will five 0 to the same numbers
# So in the end we will get number that appears only once.
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for x in nums:
        res ^= x
    return res



if __name__ == "__main__":
    nums = [2,2,1]
    print(singleNumber(nums))
    nums = [4,1,2,1,2]
    print(singleNumber(nums))
    nums = [1]
    print(singleNumber(nums))
