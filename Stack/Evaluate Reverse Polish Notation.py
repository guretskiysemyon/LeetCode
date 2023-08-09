

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:
# - The valid operators are '+', '-', '*', and '/'.
# - Each operand may be an integer or another expression.
# - The division between two integers always truncates toward zero.
# - There will not be any division by zero.
# - The input represents a valid arithmetic expression in a reverse polish notation.
# - The answer and all the intermediate calculations can be represented in a 32-bit integer.

# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# If the list[i] is a number that add it to stack.
# Else list[i] is a operator so we'll pop two number a,b 
# and calculate a (list[i]) b and push to the stack.
def evalRPN(tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
                case _ :
                    stack.append(int(t))

        return stack[0]




if __name__ == "__main__":
    tokens = ["2","1","+","3","*"]
    print(evalRPN(tokens))
    tokens = ["4","13","5","/","+"]
    print(evalRPN(tokens))
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))