

'''
Author: Semyon Guretskiy
'''

'''
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Solution:
    Uses two-pointer technique for in-place array modification:
    - last_index: points to position where next unique element should go
    - i: scans through array finding unique elements
    
    Key points:
    - Array is already sorted, so duplicates are adjacent
    - Only move elements when a new unique value is found
    - First element is always unique
    
    Time Complexity: O(n) 
    Space Complexity: O(1) - in-place modification
'''

def removeDuplicates(nums: list[int]) -> int:
    # Handle empty array
    if not nums:
        return 0
    
    # Position for next unique element
    last_index = 1
    
    # Scan array starting from second element
    for i in range(1, len(nums)):
        # Found new unique element
        if nums[i] != nums[i-1]:
            nums[last_index] = nums[i]
            last_index += 1
            
    return last_index

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = removeDuplicates(nums)
    print(f"Unique elements: {result}")
    print(f"Modified array: {nums}")
    # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]