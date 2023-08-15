

#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Link: https://leetcode.com/problems/longest-consecutive-sequence/

# Add all numbers to a set. Iterate through the set.
# - If (x-1) is not in the set, then find the longest sequence starting from the current element.
# - If (x-1) is in the set, then we have already counted 'x' as part of a sequence starting from (x-1),
#   so there's no need to calculate for 'x'. 
# Finally, return the maximum sequence length.
def longestConsecutive(nums: list[int]) -> int:
    setNums = set(nums)
    maximum = 0

    for x in setNums:
        # x is not part of previous sequence.
        if (x-1) not in setNums:
            length = 1
            while (x+length) in setNums:
                length += 1
            maximum = max(maximum, length)            
    
    return maximum
    


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(longestConsecutive(nums))
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(longestConsecutive(nums))
    nums = [0]
    print(longestConsecutive(nums))
    nums = [0,-1]
    print(longestConsecutive(nums))
    