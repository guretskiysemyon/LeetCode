
'''
Author: Semyon Guretskiy
'''


'''
80. Remove Duplicates from Sorted Array II
Medium
Given a sorted array nums, remove duplicates so each element appears at most twice.
Return k elements after placing the final result in the first k slots.

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

Solution:
    Uses two-pointer approach to track write position and reading position.
    Key idea: Compare current element with element two positions behind write pointer.
    If different, element is valid (either unique or second occurrence).
    
    Time: O(n)
    Space: O(1)
'''

def removeDuplicates(nums: list[int]) -> int:
    # Arrays of length 2 or less will already meet criteria
    if len(nums) <= 2:
        return len(nums)

    # Start from third position since first two elements are always valid
    write_pos = 2
    for read_pos in range(2, len(nums)):
        # If current number differs from number two positions back
        # it's either unique or second occurrence
        if nums[read_pos] != nums[write_pos-2]:
            nums[write_pos] = nums[read_pos]
            write_pos += 1
    
    return write_pos

# Test cases
test_cases = [
    [1,1,1,2,2,2,3,3,3,3,5,6,6],  # Mixed duplicates
    [1,1,1,2,2,3]                  # Simple case
]

for nums in test_cases:
    k = removeDuplicates(nums)
    print(f"k: {k}, nums: {nums}")
