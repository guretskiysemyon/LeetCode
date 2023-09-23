
# Author:  Semyon Guretskiy 

# 739. Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have
# to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Link: https://leetcode.com/problems/daily-temperatures/description/



# Solution:
# For each day i, compare the temperature temperatures[i] with the temperature at the top of the stack (stack[-1][0]).
# 1. If the current temperature cur is greater than or equal to the temperature at the top of the stack,
#  pop elements from the stack until either the stack is empty or you find a warmer temperature.
#  While popping elements, calculate the number of days until the warmer day 
#  by subtracting the current index i from the index of the warmer day (stack[-1][1]). Update res[i] accordingly.
# 2. Push the current temperature and its index onto the stack.
# Repeat steps for each day, effectively updating the result list res with the number of days until a warmer day for each day.
# Finally, return the res list, which contains the desired information.

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    stack = []
    res  = [0] * n

    for i in range(n-1, -1, -1):
        cur = temperatures[i]
        while stack and (cur >= stack[-1][0]):
            stack.pop()

        if stack:
            res[i] = stack[-1][1] - i
        
        stack.append((temperatures[i], i))
    
    return res


# The same solution but in different order traversal.
def dailyTemperaturesTwo(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []

    for ind, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = ind - stackInd
        stack.append((temp, ind))
    return res
            



if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(dailyTemperatures(temperatures))
    print(dailyTemperaturesTwo(temperatures))
    temperatures = [30,40,50,60]
    print(dailyTemperatures(temperatures))
    print(dailyTemperaturesTwo(temperatures))
    temperatures = [30,60,90]
    print(dailyTemperatures(temperatures))
    print(dailyTemperaturesTwo(temperatures))