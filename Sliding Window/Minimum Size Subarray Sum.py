'''
Author: Semyon Guretskiy
'''

'''
209. Minimum Size Subarray Sum
Medium
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Constraints:
- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

Link: https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150

Solution:
The problem can be solved using the sliding window technique:

1. Use two pointers (left and right) to maintain a window
2. Expand window by moving right pointer until sum >= target
3. Contract window by moving left pointer while sum >= target
4. Track minimum window size seen so far
5. Repeat until right pointer reaches end

Time Complexity: O(n) where n is length of nums array
- Each element is added and removed at most once

Space Complexity: O(1) 
- Only using constant extra space for variables

Example with nums = [2,3,1,2,4,3], target = 7:
1. [2] -> sum = 2 < 7
2. [2,3] -> sum = 5 < 7
3. [2,3,1,2] -> sum = 8 >= 7, contract: [3,1,2] -> sum = 6 < 7
4. [3,1,2,4] -> sum = 10 >= 7, contract: [1,2,4] -> sum = 7 >= 7, contract: [2,4] -> sum = 6 < 7
5. [2,4,3] -> sum = 9 >= 7, contract: [4,3] -> sum = 7 >= 7, contract: [3] -> sum = 3 < 7
Answer: 2 (subarray [4,3])
'''

def minSubArrayLen(target: int, nums: list[int]) -> int:
   # Handle case where first element meets target
   if nums[0] >= target:
       return 1

   # Initialize variables for sliding window
   left = 0
   current_sum = 0
   # Set minimal to impossible value for comparison
   minimal = len(nums) + 1
   
   # Expand window with right pointer
   for right in range(len(nums)):
       # Add new element to window
       current_sum += nums[right]
      
       # If sum meets target, try to minimize window
       if current_sum >= target:
           # Contract window while sum still meets target
           while current_sum >= target:
               current_sum -= nums[left]
               left += 1
           # Update minimal length (+2 because we moved left one step too far)    
           minimal = min(minimal, right - left + 2)
   
   # Return 0 if no solution found, otherwise return minimal length        
   if minimal == len(nums) + 1:
       return 0
   return minimal

# Test cases
target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))  # Expected: 2

target = 4
nums = [1,4,4]
print(minSubArrayLen(target, nums))  # Expected: 1

target = 11
nums = [1,1,1,1,1,1,1,1]
print(minSubArrayLen(target, nums))  # Expected: 0

target = 7
nums = [6,7,7,6,1,5,2,3]
print(minSubArrayLen(target, nums))  # Expected: 1