
# Author:  Semyon Guretskiy

# 853. Car Fleet

# There are n cars going to the same destination along a one-lane road.
# The destination is target miles away.

# You are given two integer array position and speed, both of length n,
# where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it
# and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed.
# The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed.
# Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
# Return the number of car fleets that will arrive at the destination.

# Link: https://leetcode.com/problems/car-fleet/description/

# Solution:
# 1. Create a sorted list in reverse order  of tuples data, where each tuple contains the initial position and speed of a car. 

# 2. Initialize a variable count to 1. This variable will keep track of the number of car fleets formed. 
# You start with one fleet because the first car (the one with the highest initial position)
# is always considered as the lead car of the first fleet.

# 3. Calculate the time it takes for the lead car (the first car in the sorted list) 
# to reach the target using the formula flee_speed = (target - data[0][0]) / data[0][1]. 
# This calculates the time it takes for the lead car to reach the target at its speed. 
# Iterate through the rest of the cars in the data list. 

# 4. For each car, calculate the time cur it takes to reach the target using the same formula.

# 5. Compare the cur time with the flee_speed. If cur is greater than flee_speed, 
# it means the current car cannot catch up with the lead car and forms a new car fleet. 
#Increment the count by 1, and update flee_speed to the current cur.

# After the loop, return the final value of count, which represents the total number of car fleets
# that can reach the target without any car overtaking another car in the same fleet.

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    n = len(position)

    if n == 0:
        return 0
    
    data = [(position[i], speed[i]) for i in range(n)]
    data.sort(reverse=True)
    
    count = 1
    flee_speed = (target - data[0][0])/ data[0][1]
    for i in range(1, n):
        cur = (target - data[i][0])/ data[i][1]

        if cur > flee_speed:
            count += 1
            flee_speed = cur
    
    
    return count



if __name__ == "__main__":
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]
    ans = carFleet(target, position, speed)
    print(ans)
    target = 10
    position = [3]
    speed = [3]
    ans = carFleet(target, position, speed)
    print(ans)
    target = 100
    position = [0,2,4]
    speed = [4,2,1]
    ans = carFleet(target, position, speed)
    print(ans)
    