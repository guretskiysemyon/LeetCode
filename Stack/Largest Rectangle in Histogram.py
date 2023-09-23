



# 84. Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/


# Solution: 
# Find for each element x the first element that smaller than x from both right and left.
# Now itherate through and calculate the maximum area.
def largestRectangleArea(heights: list[int]) -> int:
    right = [len(heights) ] * len(heights)
    stack = []
    maxArea = 0


    for ind, height in enumerate(heights):
        while stack and height <= stack[-1][0]:
            stackT, stackInd = stack.pop()
            right[stackInd] = ind
        stack.append((height, ind))

    stack = []
    for i, h in enumerate(heights):
        while stack and h <= stack[-1][0]:
            stack.pop()
        if stack:
            maxArea = max(h * (right[i] - stack[-1][1] - 1), maxArea)
        else:
            maxArea = max(h * (right[i] - 0), maxArea)
        stack.append((h, i))
    
    return maxArea



if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print(largestRectangleArea(heights))
    heights = [2,4]
    print(largestRectangleArea(heights))

 