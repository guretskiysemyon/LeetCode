
'''
Author: Semyon Guretskiy
'''

'''
88. Merge Sorted Array
Easy
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Solution:
    Uses three-pointer approach to merge arrays from right to left:
    - curr1: tracks position in nums1
    - curr2: tracks position in nums2
    - last: tracks insertion position
    
    Time Complexity: O(m+n)
    Space Complexity: O(1) - in-place merge
'''

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    # Initialize pointers to end of valid elements
    curr1 = m - 1  # Last element in nums1
    curr2 = n - 1  # Last element in nums2
    last = m + n - 1  # Last position in merged array

    # Merge arrays from right to left
    while curr2 >= 0 and curr1 >= 0:
        if nums2[curr2] >= nums1[curr1]:
            nums1[last] = nums2[curr2]
            curr2 -= 1
        else:
            nums1[last] = nums1[curr1]
            nums1[curr1] = 0  # Clear original position
            curr1 -= 1
        last -= 1

    # Copy remaining elements from nums2 if any
    while curr2 >= 0:
        nums1[last] = nums2[curr2]
        curr2 -= 1
        last -= 1

if __name__ == "__main__":
    # Test case 1: Normal merge
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge(nums1, 3, nums2, 3)
    print(nums1)  # [1,2,2,3,5,6]

    # Test case 2: Empty nums1
    nums1 = [0]
    nums2 = [1]
    merge(nums1, 0, nums2, 1)
    print(nums1)  # [1]