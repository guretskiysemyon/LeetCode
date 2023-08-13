

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
# Link: https://leetcode.com/problems/contains-duplicate/

# Using hash map we can fins the duplicate.
# Iterate through a array and check if there is an element with the same value in map
# if there is return False, else add this element to map.
def containsDuplicate(nums):
    dict = {}
    for x in nums:
        k = dict.get(x)
        if k is not None:
            return True
        dict[x]=1
    return False



if __name__ == "__main__":
    nums = [1,2,3,1]
    print(containsDuplicate(nums))
    nums = [1,2,3,4]
    print(containsDuplicate(nums))
    nums = [1,1,1,3,3,4,3,2,4,2]
    print(containsDuplicate(nums))
