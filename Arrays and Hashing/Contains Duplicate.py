

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
# Link: https://leetcode.com/problems/contains-duplicate/

# Using a hash map, we can find duplicates in an array. 
# Iterate through the array and check if an element with the same value exists in the map. 
# If it does, return False; otherwise, add the element to the map.
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
