


# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Link: https://leetcode.com/problems/group-anagrams/description/


import collections


# Solution by using hash map.
# So we create list [0] * 26 for every string in strs s.t in index i in list will be
# j if i'th letter of english alphabet appears j times in current string s.
# For example for word "abac" we got [2,1,1,0,...,0].
# Then we use this list as unique key for dictionary, and value will be list contains strings in strs that
# got the same key. In the end we return values of dictionary.
def groupAnagramsHash(strs: list[str]) -> list[list[str]]:
    ans_map = collections.defaultdict(list)     # create default values as list

    for s in strs:
        alphabet =  [0] * 26    # create a key
        for x in s:
            alphabet[ord(x)-97] += 1
        
        ans_map[tuple(alphabet)].append(s)  # add in the map

    return ans_map.values()



# In this solution sorted strings wiil be used. After we sort two strings that are anagrams
# we will get the same string and can use it as a key for dictionary.
def groupAnagramsSortedString(strs: list[str]) -> list[list[str]]:
    ans_map = collections.defaultdict(list)

    for s in strs:
        sorted_s = ''.join(sorted(s))   # sort and copy string
        ans_map[sorted_s].append(s)
    
    return ans_map.values()



if __name__=="__main__":
    # copyandsort()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagramsSortedString(strs))
    strs = [""]
    print(groupAnagramsSortedString(strs))
    strs = ["a"]
    print(groupAnagramsSortedString(strs))
    strs = ["", ""]
    print(groupAnagramsSortedString(strs))
