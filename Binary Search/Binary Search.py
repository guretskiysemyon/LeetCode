
'''
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Link: https://leetcode.com/problems/binary-search/description/

'''



def search(nums, target):
    if len(nums)==0:
        return -1
    i = 0
    j = len(nums)-1
    while i <= j:
        n = (i+j)//2
        if nums[n] == target:
            return n
        elif nums[n] > target:
            j = n-1
        else:
            i = n + 1
    return -1


if __name__=="__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    search(nums, target)