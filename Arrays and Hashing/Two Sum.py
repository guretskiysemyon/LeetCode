
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Link: https://leetcode.com/problems/two-sum/


# Iterate through 'nums' and add every element to a hash map. 
# Then, iterate through 'nums' again and for every element 'x', check if the value 'target - x' exists in the hash map.
# Return 'True' if we find that 'target - x' is in the map.
def twoSum(nums, target):
        map = {}
        n = len(nums)
        for i in range(n):
            map[nums[i]] = i

        for i in range(n):
            res = map.get(target - nums[i])
            if res is None or res == i:
                continue
            return [i, res]
        return []




if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print(twoSum(nums, target))
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))
    nums = [3,3]
    target = 6
    print(twoSum(nums, target))