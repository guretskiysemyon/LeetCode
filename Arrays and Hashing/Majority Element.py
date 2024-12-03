'''
Author: Semyon Guretskiy
'''


'''
169. Majority Element
Easy
Given an array nums of size n, return the majority element.
The majority element appears more than ⌊n / 2⌋ times.

Link: https://leetcode.com/problems/majority-element/description/

Solution:
    Uses Boyer-Moore Voting Algorithm:
    - Maintain a candidate element and its count
    - When count reaches 0, pick new candidate
    - Majority element will always win due to appearing more than n/2 times
    
    Why it works:
    - If we cancel out each occurrence of an element with different elements,
      the majority element will remain as it appears more than n/2 times
    
    Time Complexity: O(n)
    Space Complexity: O(1)
'''

def majorityElement(nums: list[int]) -> int:
    # Initialize candidate and its count
    majority_element = None
    count = 0

    # Process each element
    for num in nums:
        if majority_element == num:
            # Found another occurrence of current candidate
            count += 1
        elif count == 0:    
            # No current candidate, set new one
            count = 1
            majority_element = num
        else:
            # Different element, reduce count
            count -= 1
            
    return majority_element

if __name__ == "__main__":
    # Test case 1: Simple majority
    nums = [3,2,3]
    result = majorityElement(nums)
    print(f"Majority element: {result}")  # Expected: 3

    # Test case 2: Multiple occurrences
    nums = [2,2,1,1,1,2,2]
    result = majorityElement(nums)
    print(f"Majority element: {result}")  # Expected: 2