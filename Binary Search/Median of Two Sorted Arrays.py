'''
Author: Semyon Guretskiy
'''

'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/


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