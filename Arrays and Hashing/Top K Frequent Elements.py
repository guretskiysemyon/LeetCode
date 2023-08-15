
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

# Link: https://leetcode.com/problems/top-k-frequent-elements/

# - First, iterate through the 'nums' list and count the number of times each value appears in the list. 
#    Store this information in a dictionary, and also create an array of lists named 'arr'. (List of lists because
#    can be more that one value with the same number of appearances).
# - Second, iterate through the dictionary and for each key-value pair,
#    store the key in the 'arr' list at the index equal to the value.
# - Now, the 'arr' array contains the most frequent numbers from 'nums',
#    sorted in ascending order based on the number of their appearances.
# - Finally, iterate through the 'arr' list from the end to the beginning and return the first 'k' numbers."
def topKFrequent(nums, k):
        h = {}
        n = len(nums)
        arr = [[] for i in range(n + 1)]
        res =[]

        for x in nums:
            h[x] = h.get(x, 0) + 1
        
        for key,val in h.items():
            arr[val].append(key)

        for i in range(n, 0, -1):
            for x in arr[i]:
                res.append(x)
                if len(res) == k:
                    return res
                


if __name__== "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums,k))
    nums = [1]
    k = 1
    print(topKFrequent(nums,k))