'''
Author: Semyon Guretskiy
'''

'''
2221. Find Triangular Sum of an Array
Medium

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:
1. Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
2. For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
3. Replace the array nums with newNums.
4. Repeat the entire process starting from step 1.

Return the triangular sum of nums.

Link: https://leetcode.com/problems/find-triangular-sum-of-an-array/description/

Solution:
This problem can be solved in two ways:

1. Iterative Approach (First Solution):
  - Modify array in-place by calculating sums of adjacent elements
  - Time Complexity: O(n²) where n is length of input array
  - Space Complexity: O(1) as we modify array in-place

2. Mathematical Approach using Pascal's Triangle (Second Solution):
  - Uses the fact that final sum follows Pascal's Triangle pattern and calculate coefficients for each number's contribution to final sum.
  - Time Complexity: O(n)
  - Space Complexity: O(1)

Example with [1,2,3,4]:
Step 1: [3,5,7]  # (1+2)%10, (2+3)%10, (3+4)%10
Step 2: [8,2]    # (3+5)%10, (5+7)%10
Step 3: [0]      # (8+2)%10

The first solution is more intuitive while second is more efficient for large arrays.
'''

def triangularSum(nums: list[int]) -> int:
   # Keep track of current array size
   n = len(nums) - 1
   
   # Continue until only one element remains
   while n >= 1:
       # Calculate sum of adjacent elements
       for i in range(n):
           nums[i] = (nums[i] + nums[i+1]) % 10
       n -= 1

   return nums[0]


def triangularSum(nums: list[int]) -> int:
   # Handle base case
   n = len(nums)
   if n == 1:
       return nums[0] % 10
   
   # Initialize coefficient for Pascal's Triangle
   coefficient = 1
   result = 0
   
   # Process pairs of elements from both ends
   for i in range(n // 2):
       # Add contribution from both ends multiplied by coefficient
       result += coefficient * nums[i]
       result += coefficient * nums[n - 1 - i]
       
       # Calculate next coefficient using combination formula
       coefficient = coefficient * (n - 1- i) // (i + 1)

   # Handle middle element for odd length arrays
   if n % 2 == 1:
       result += coefficient * nums[n // 2]
   
   return result % 10


# Test cases
numbers = [4,5,6,7]
print(triangularSum(numbers))  # Expected: 0

numbers = [1,2,3,4,5]
print(triangularSum(numbers))  # Expected: 8

numbers = [4,5]
print(triangularSum(numbers))  # Expected: 9