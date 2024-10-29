


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Constraints:
# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

# Link: https://leetcode.com/problems/group-anagrams/description/


import collections


# Here's a solution using a hash map. For each string in the 'strs' list, we create a list [0] * 26.
# In this list, the value at index i represents how many times the i-th letter(starting from 0) of the English alphabet
# appears in the current string. For example, the word 'abac' would result in the list [2, 1, 1, 0, ..., 0],
# reflecting the letter counts.
# Next, we use these lists as unique keys for a dictionary, 
# and the corresponding values are lists containing strings from 'strs' that share the same key. 
# In the end, we return the values of the dictionary.
def groupAnagramsHash(strs: list[str]) -> list[list[str]]:
    ans_map = collections.defaultdict(list)     # create default values as list

    for s in strs:
        alphabet =  [0] * 26    # create a key
        for x in s:
            alphabet[ord(x)-97] += 1
        
        ans_map[tuple(alphabet)].append(s)  # add in the map

    return ans_map.values()



# In this solution, we use sorted strings. When we sort two strings that are anagrams, 
# they become identical, and we can then use them as keys for a dictionary
def groupAnagramsSortedString(strs: list[str]) -> list[list[str]]:
    ans_map = collections.defaultdict(list)

    for s in strs:
        sorted_s = ''.join(sorted(s))   # sort and copy string
        ans_map[sorted_s].append(s)
    
    return ans_map.values()



if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagramsSortedString(strs))
    strs = [""]
    print(groupAnagramsSortedString(strs))
    strs = ["a"]
    print(groupAnagramsSortedString(strs))
    strs = ["", ""]
    print(groupAnagramsSortedString(strs))
