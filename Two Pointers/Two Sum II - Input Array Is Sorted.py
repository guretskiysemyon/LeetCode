
# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2,
# added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


# Solution:
# One pointer to the beginning and the second to the end.
# Check the sum of the elements that the pointers point at.

# If the sum is bigger than the target, we want to move the right pointer to try a smaller number.
# If the sum is smaller than the target, we want to move the left pointer to try a bigger number.
# If the sum is equal to the target, we return the indices of those pointers in the array.

# We can do this search because the array is sorted in increasing order.

def twoSum(numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            k = numbers[i] + numbers[j]
            if k > target:
                j -= 1
            elif k < target:
                i += 1
            else:
                return [i+1, j+1]
            



if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9
    print(twoSum(numbers, target))

    numbers = [2,3,4]
    target = 6
    print(twoSum(numbers, target))

    numbers = [-1,0]
    target = -1
    print(twoSum(numbers, target))
