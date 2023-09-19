

# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Link: https://leetcode.com/problems/valid-palindrome/description/

# Solution
# The idea is simple: to use two pointers and run them toward the middle
# and check if the characters are the same. But there are some restrictions:
# 1. Case ignorance
# 2. We need to ignore whitespace and so on.
# The solution is to check everything in lowercase and move the pointers through white spaces
# until they arrive at a numeral or letter character.

def isPalindrome(s: str) -> bool:
    n = len(s)
    if n == 1:
        return True
    i = 0
    j = n - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while j > i and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True



def isPalindrome_two(s):
    s = s.lower()
    letters = []
    for x in s:
        if x.isalnum():
            letters.append(x)

    n = len(letters)
    ran = n // 2
    for i in range(ran):
        if letters[i] != letters[n-1-i]:
            return False
    return True


# To use an array and save in it all numeric-letter characters,
# and then use two pointers to check if it's a palindrome.
if __name__=="__main__":
    print("First")
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s) == True)
    s = "race a car"
    print(isPalindrome(s) == False)
    s = " "
    print(isPalindrome(s)==True)

    print("Second")
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome_two(s) == True)
    s = "race a car"
    print(isPalindrome_two(s) == False)
    s = " "
    print(isPalindrome_two(s)==True)




 