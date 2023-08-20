
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


# Initialize two pointers, i = 0 and j = n-1. Then iterate through the array and check:
# - If numbers[i] + numbers[j] equals the target, return i, j.
# - If numbers[i] + numbers[j] is greater than the target, decrement j to try a smaller number.
# - If numbers[i] + numbers[j] is less than the target, increment i to try a greater number.

def twoSum(numbers: list[int], target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if sum == target:
            return [i+1,j+1]
        elif sum < target:
            i += 1
        else:
            j -= 1


if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers,target))
    numbers = [2,3,4]
    target = 6
    print(twoSum(numbers,target))
    numbers = [-1,0]
    target = -1
    print(twoSum(numbers,target))
