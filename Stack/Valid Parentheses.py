


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.

# Link: https://leetcode.com/problems/valid-parentheses/



# Idea is to use a stack. The string of parantheses is legal if every time we point
# on closing bracket on the top of the stack should be opening bracket of the same type.
# Also in the end stask must be empty.
def isValid(s):
        # Check there is a even number of symbols in s.
        if len(s) % 2 != 0:
            return False
        
        #Create stack and and dictionary.
        stack = []
        couple = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in "({[":                                          # If c is one of the opening brackets add to stack.
                stack.append(c)
            elif not stack or c != couple.get(stack.pop()):         # Else check that on top of the stack there is the bracket of
                return False                                        # of the same type as c.
        return not stack





if __name__ == "__main__":
    s = "()"
    print(isValid(s))
    s = "()[]{}"
    print(isValid(s))
    s = "(]"
    print(isValid(s))
