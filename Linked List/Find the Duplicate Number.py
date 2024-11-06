'''
Author: Semyon Guretskiy
'''

'''
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.


Link: https://leetcode.com/problems/find-the-duplicate-number/description/


Solution:
This problem can be solved using Floyd's Cycle Finding Algorithm by treating the array as a linked list. 
Since each number in the array is in range [1, n], we can use nums[i] as a pointer to the next index. 
Due to the pigeonhole principle, there must be a cycle in this "linked list" due to the duplicate number.

The algorithm works in two phases:
1. Detect the intersection point inside the cycle using two pointers (fast and slow)
2. Find the entrance to the cycle, which is our duplicate number, by moving one pointer to start
   and moving both pointers at the same speed until they meet
'''



def findDuplicate(nums: list[int]) -> int:
    
   
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    
    return slow



if __name__ == "__main__":
    nums = [1,1]
    res = findDuplicate(nums)
    print(res)

    nums = [1,3,4,2,2]
    res = findDuplicate(nums)
    print(res)

    nums = [3,1,3,4,2]
    res = findDuplicate(nums)
    print(res)

    nums = [3,3,3,3,3]
    res = findDuplicate(nums)
    print(res)

    nums = [1, 2 ,3, 2, 4, 5]
    res = findDuplicate(nums)
    print(res)

