

# Author: Semyon Guretskiy

# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Link: https://leetcode.com/problems/generate-parentheses/description/?source=submission-ac

# Solution:
# The backtrack() function recursively explores all possible combinations of parentheses,
# starting with the current count of open and closed parentheses.
# It adds an open parenthesis if the count of open parentheses is less than the input value n, 
# and it adds a closed parenthesis if the count of closed parentheses is less than the count of open parentheses.
def generateParenthesis(n: int) -> list[str]:
    result = []
    cur_seq = []

    def backtrack(open, closed):
        if open == closed == n:
            result.append("".join(cur_seq))

        if open < n:
            cur_seq.append("(")
            backtrack(open + 1, closed)
            cur_seq.pop()
        if closed < open:
            cur_seq.append(")")
            backtrack(open, closed + 1)
            cur_seq.pop()
    
    backtrack(0,0)

    return result


# Same solution without stack and with string.
def generateParenthesisWithoutStack(n: int) -> list[str]:
    result = []

    def backtrack(open, closed, cur_seq):
        if open == closed == n:
            result.append(cur_seq)

        if open < n:
            backtrack(open + 1, closed, cur_seq + "(")
        if closed < open:
            backtrack(open, closed + 1, cur_seq + ")")
    
    backtrack(0,0, "")

    return result


if __name__ == "__main__":
    n = 3
    res = generateParenthesis(n)
    print(res)
    res = generateParenthesisWithoutStack(n)
    print(res)