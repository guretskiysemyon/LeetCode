

'''42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Link: https://leetcode.com/problems/trapping-rain-water/description/


Solution: 
We need to calculate the amount of water that is trapped between buildings. To achieve this, we will employ the two-pointer method. 

The first pointer, 'l' (left one), will indicate a specific building,
while the second pointer, 'r' (right one), will iterate through the list until it encounters a building with the same height or higher as 'l',
or until 'r' reaches the end of the list. Additionally, we will sum all the heights of buildings that 'r' passes by.

When the height of 'r' is greater than or equal to the height of 'l',
we will compute the amount of trapped water between 'r' and 'l'.
We will take the length of the interval between the buildings, multiply it by the height of 'l',
and then subtract the total of all the heights summed earlier. 
This calculation will provide the answer for this specific interval. We'll then move 'l' to be equal to 'r' and increment 'r' by 1 to continue.

Stopping here would result in missing some of the water, as 'r' reaches the end of the list and the loop stops.
To address this, we repeat the process in the reverse direction, from the end to the beginning,
with a slight modification in the condition. Here, we check that the height of 'l' is significantly smaller than the height of 'r',
ensuring we count the same interval only once. The code will be adjusted according to the logic of the algorithm.

In summary, we visit each building at most O(1) times, making the algorithm operate in O(n) complexity.


I've made some grammar and clarity adjustments to help better convey the intended meaning.
If you have any further questions or need additional help, feel free to ask!'''


def trap(height: list[int]) -> int:
    n = len(height)
    if n <= 2:
        return 0
    
    l = 0
    r = 1
    sum = 0
    h = 0
    while r < n:
        if height[r] >= height[l]:
            sum +=  (r - l - 1) * height[l] - h
            l = r
            r += 1
            h = 0
        else:
            h += height[r]
            r += 1
    
    h = 0
    r = n-1
    l = n-2
    while l > -1:
        if height[r] < height[l]:
            sum +=  (r - l - 1) * height[r] - h
            r = l
            l -= 1
            h = 0
        else:
            h += height[l]
            l -= 1
    
    return sum


     
def fff(height):
    if not height:
            return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res


if __name__=="__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))
    height = [4,2,0,3,2,5]
    print(trap(height))
    height = [2,0,2]
    print(trap(height))

    height = [10, 0, 2, 7, 2 ,1]
    fff(height)