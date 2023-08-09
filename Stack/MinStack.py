
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# - MinStack() initializes the stack object.
# - void push(int val) pushes the element val onto the stack.
# - void pop() removes the element on the top of the stack.
# - int top() gets the top element of the stack.
# - int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Link: https://leetcode.com/problems/min-stack/


# Idea of solution is tu use to stacks. One for general purpose and the second one for keeping minimum.
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    # First, add to general stack and add to minimum_stack only if val less or equal to 
    # number on the top of minimm_stack. For empty stack the condition will always be true.
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    # Pop element from the stack and if elemnt is current minimum that pop it too.
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    # As in regular stack.
    def top(self):
        return self.stack[-1]

    # Return value of the current minimum.
    def getMin(self):
        return self.min_stack[-1]
    
