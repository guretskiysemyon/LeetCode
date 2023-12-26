

'''
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


Solution:
We are going to employ binary search. The condition guiding our search is as follows:
If the middle element is less than the rightmost element, then the minimum resides on the left side.
Otherwise, if the middle element is greater than or equal to the rightmost element, then the minimum is situated on the right side.
'''

def findMin(nums: list[int]) -> int:
    i = 0
    j = len(nums) - 1
    minimum = 5001

    while i <= j:
        n = (i + j) // 2
        minimum = min(minimum, nums[n])

        # minimum is on the right side
        if nums[n] > nums[j]:
            i = n + 1
        # minimum is on the left side
        else:
            j = n - 1
    
    return minimum




if __name__=="__main__":
    # nums = [3,4,5,1,2]
    # print(findMin(nums))
    nums = [4,5,6,7,8,0,1,2,3]
    print(findMin(nums))
    nums = [11,13,15,17]
    print(findMin(nums))
    nums = [11]
    print(findMin(nums))
    nums = [2,1]
    print(findMin(nums))

