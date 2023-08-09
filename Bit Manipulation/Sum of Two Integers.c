#include "stdio.h"

/*
 Given two integers a and b, return the sum of the two integers without using the operators + and -.

*/


// Simulate the addition gate by two opperations "and" and "xor"
int getSum(int a, int b){
    int carry;
    while (b != 0) {
            carry = a & b;
            a ^= b;
            b = carry << 1;

    }

     return a;
}



int main(int argc, char const *argv[]){
        int a = 1;
        int b = 2;
        printf("%d\n", getSum(a,b));
        a = 2;
        b = 3;
        printf("%d\n", getSum(a,b));
}
