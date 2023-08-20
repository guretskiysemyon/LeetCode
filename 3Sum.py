

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Link: https://leetcode.com/problems/3sum/description/


# Iterate through each element in the array 
# and search for the negation of nums[i] using the 2Sum algorithm approach.
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans = []
    n = len(nums)
    i = 0

    while i < n:
        # For element in index i create left and right
        target = - nums[i]
        l = i + 1
        r = n - 1
        while l < r:
            # calculate current sum
            sum = nums[l] + nums[r]
            if sum < target:
                l += 1
            elif sum > target:
               r -= 1
            else:
                # if tripplet has been found then append.
                ans.append([nums[i], nums[l], nums[r]])

                # Skip all duplicates of nums[l] and nums[r]
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l+=1
                r -= 1
                while nums[r] == nums[r+1] and l < r:
                    r -=1
        # skip all duplicates
        i += 1
        while i < n and nums[i] == nums[i-1]:
            i+=1 

    return ans




        
    


if __name__ =="__main__":
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))
    nums = [0,0,0]
    print(threeSum(nums))
    nums = [0,1,1]
    print(threeSum(nums))
    nums = [0,0,0,0]
    print(threeSum(nums))
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(threeSum(nums))

