'''
Author: Semyon Guretskiy
'''

'''
27. Remove Element
Easy
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements which are not equal to val.

Link: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

Solution:
    Uses two-pointer technique:
    - left: tracks position for next place to write element
    - i: scans through array

    The code iterates through the array, and when it finds an element equal to val,
    it does not change left. Otherwise, it writes the current element to nums[left] and increments left by 1.
    Along the way, it counts the number of elements that differ from val.
    
    Time: O(n)
    Space: O(1)
'''

def removeElement(nums: list[int], val: int) -> int:
    # Position for next non-val element
    left = 0

    # Scan through array
    for i in range(len(nums)):
        # Skip val elements
        if nums[i] == val:
            continue
        
        # Move non-val element if needed
        if left != i:       
            nums[left] = nums[i]
        left += 1
            
    return left

# Test
nums = [3,2,1,3]
val = 3
print(f"Elements remaining: {removeElement(nums, val)}")
print(f"Modified array: {nums}")