

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Link: https://leetcode.com/problems/product-of-array-except-self/

The idea is to create an array of prefix products and an array of suffix products.
For each element at index 'i' in 'nums', the result of the product of all elements except itself
will be 'prefix[i-1] * suffix[i+1]'. 
In this function, we can avoid using the second array because of all needed data is available during the second loop, 
and it allows us to calculate the result while computing the suffix products.
In the end, we return the resulting array.
'''
def productExceptSelf(nums):
        n = len(nums)
        res = [1 for i in range(n)]
        left_mult = 1
        right_mult = 1
        for k in range(n):
            res[k] = left_mult
            left_mult *= nums[k]

        for l in range(n - 1, -1 , -1):
            res[l] *= right_mult
            right_mult *= nums[l]


        return res



if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf(nums))
    nums = [-1,1,0,-3,3]
    print(productExceptSelf(nums))
