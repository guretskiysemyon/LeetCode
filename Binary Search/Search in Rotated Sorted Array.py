'''
Author: Semyon Guretskiy
'''

'''
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
 such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
   For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/


Solution:
We can apply a modified binary search, adapting the conditions based on whether the array has been rotated and where the minimum might lie.

First, if the array is rotated such that the minimum element is in the left half, e.g., `[5, 6, 0, 1, 2, 3, 4]`, 
we can check this by verifying `nums[left] > nums[middle]`.

1. If `nums[left] > nums[middle]`, it means the minimum element is in the left half. 
   - If the target is greater than or equal to `nums[left]` or less than `nums[middle]`, we continue the search in the left half.
   - Otherwise, we search in the right half.

2. If the minimum is not in the left part, then the left half is sorted in ascending order, and we can proceed with a standard binary search.
   - Check if `target >= nums[left]` or `target < nums[middle]`. If either condition holds, the target might be in the left half, so we adjust the search to that side.

This approach ensures we always discard half of the search space, achieving O(log n) complexity.
'''

def binary_search_rotated_array(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        middle = (left + right) // 2
        
        # Check if the middle element is the target
        if nums[middle] == target:
            return middle

        # If the left part is not sorted, minimum is in the left half
        if nums[left] > nums[middle]:
            # If target is greater than or equal to nums[left] or less than nums[middle], search left
            if target >= nums[left] or target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1
        # If the left half is sorted, apply regular binary search rules
        else:
            # If target is in the left half range, adjust right pointer
            if target >= nums[left] or target < nums[middle]:
                right = middle - 1
            else:
                left = middle + 1

    return -1

if __name__=="__main__":
   
    nums = [4,5,6,7,8,0,1,2,3]
    print(nums)
    for i in range(len(nums)):
        res = binary_search_rotated_array(nums, nums[i])
        if nums[i] != nums[res]:
            print(f"{i} : {nums[i]}\n{res} : {nums[res]}\n\n") 
   
    nums = [4,5,6,7,0,1,2]
    print(nums)
    for i in range(len(nums)):
        res = binary_search_rotated_array(nums, nums[i])
        if nums[i] != nums[res]:
            print(f"{i} : {nums[i]}\n{res} : {nums[res]}\n\n") 
  
    nums = [11]
    print(nums)
    for i in range(len(nums)):
        res = binary_search_rotated_array(nums, nums[i])
        if nums[i] != nums[res]:
            print(f"{i} : {nums[i]}\n{res} : {nums[res]}\n\n") 
  
 
    nums = [2,1]
    print(nums)
    for i in range(len(nums)):
        res = binary_search_rotated_array(nums, nums[i])
        if nums[i] != nums[res]:
            print(f"{i} : {nums[i]}\n{res} : {nums[res]}\n\n") 
    
    
    nums = [5,1,3]
    print(nums)
    for i in range(len(nums)):
        res = binary_search_rotated_array(nums, nums[i])
        if nums[i] != nums[res]:
            print(f"{i} : {nums[i]}\n{res} : {nums[res]}\n\n") 

    nums = [4,5,6,7,8,1,2,3]
    print(nums)
    for i in range(len(nums)):
        res = binary_search_rotated_array(nums, nums[i])
        if nums[i] != nums[res]:
            print(f"{i} : {nums[i]}\n{res} : {nums[res]}\n\n") 

    nums = [5,1,2,3,4]
    print(nums)
    for i in range(len(nums)):
        res = binary_search_rotated_array(nums, nums[i])
        if nums[i] != nums[res]:
            print(f"{i} : {nums[i]}\n{res} : {nums[res]}\n\n") 