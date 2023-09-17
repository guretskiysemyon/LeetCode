# include "stdio.h"

// 11. Container With Most Water

/*
 You are given an integer array height of length n. 
 There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 Find two lines that together with the x-axis form a container, such that the container contains the most water.
 Return the maximum amount of water a container can store.
 Notice that you may not slant the container.
*/

// Link: https://leetcode.com/problems/container-with-most-water/description/

/*
Solution:
 The approach here utilizes two pointers, one on the left and the other on the right.

 During each iteration, we calculate the area using the formula:
 (right - left) * min(height[right], height[left]).

 The critical aspect is determining which pointer to move.
 If height[left] is greater than height[right], then we should move the right pointer.
 It's essential to note that regardless of which pointer we move, 
 in the next iteration, the (right - left) component of the area calculation will be smaller. 

 Additionally, the area is determined by the minimum value between height[right] and height[left].
 Therefore, if height[right] is less than height[left], and we decide to move the left pointer,
 the new area cannot be greater than the current one.

 For this reason, we opt to move the pointer associated with the smaller height value,
 as this approach increases the potential area

*/



int maxArea(int* height, int heightSize){
    int* l = height;
    int* r = l + heightSize - 1;
    int max = 0;
    

    while (l < r){
        int min  = *r >= *l ? *l : *r;
        int area = (r - l) * min;
        max = area > max ? area : max;
        if (*l < *r)
            l++;
        else
            r--;
    }
        
    return max;
}

int main(int argc, char const *argv[])
{
    int height[9] = {1,8,6,2,5,4,8,3,7};
    int max = maxArea(&height, 9);
    printf("%d\n", max);
    return 0;
}
