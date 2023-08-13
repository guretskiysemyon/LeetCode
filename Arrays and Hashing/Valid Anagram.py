


# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Link: https://leetcode.com/problems/contains-duplicate/


# Create two hash maps.
# Iterate through s and add every element to map as key and
# and number of times this element appears in s will be the value.
# Do the same for t. And check if two maps are equel and return unswer
def isAnagram(s, t):
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for x in s:
            s_map[x] = s_map.get(x, 0) + 1

        for y in t:
            t_map[y] = t_map.get(y, 0) + 1

        return t_map == s_map


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))
    s = "rat"
    t = "car"
    print(isAnagram(s,t))
