#include "stdio.h"

/*
 Given a signed 32-bit integer x, return x with its digits reversed. 
 If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
 https://leetcode.com/problems/reverse-integer/description/
*/

// Iterate from left to right. Take left digit add to reverse number and multiply by 10 to shift it. 
// Stop when x is 0.
// Example: 123 
// first: reverse = 3 and x = 12
// second: reverse = 32 and x = 1
// third: reverse = 321 and x = 0  
int reverse(int x){
    long long reverse = 0;
    int MAX = 2147483647;
    int MIN = -2147483648;

    while (x != 0){
        reverse = reverse * 10 + x % 10;
        x = x / 10;
    }

    if (reverse < MIN || reverse > MAX)
        reverse = 0;

    return reverse;

}


int main(int argc, char const *argv[])
{  
    int x;
    x = 123;
    printf("%d\n", reverse(x));
    x = -123;
    printf("%d\n", reverse(x));
    x = 120;
    printf("%d\n", reverse(x));
}
