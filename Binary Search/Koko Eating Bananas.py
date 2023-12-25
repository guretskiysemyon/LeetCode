




'''
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Link: https://leetcode.com/problems/koko-eating-bananas/description/


Solution:
In this solution, we'll employ binary search. 
Let's acknowledge that the maximum potential speed of Koko is the highest number in the given list, while the minimum speed is 1, being the smallest natural number.
Thus, our search for the answer will be within this range.

We can break down the solution into two logical parts:

1. For a given speed 'k', our objective is to determine how much time it takes for Koko to consume all the bananas. 
    We achieve this by iterating through the entire list. For each element 'x' in the list, we calculate roundup(x / k).

2. Implementing the binary search within the specified range. 
    It's essential to note that if Koko finishes eating all the bananas within the list and still has time left,
    we should attempt a smaller number while keeping this number as a potential result. 
    There might be multiple speeds allowing Koko to consume all the bananas, and our goal is to choose the smallest among them.
    However, it's possible that we are already using the smallest speed, and if we move to the next one without saving it, we might lose this optimal solution.

The latter part of the code follows the standard binary search approach.

Complexity: O(log(max(piles))*n)

'''


def minEatingSpeed(piles: list[int], h: int) -> int:
    
    i = 1
    j = max(piles)
    res = j

    while i <= j:
        n = (i + j) // 2
        h_temp  = h
        for x in piles:
            if x % n == 0:
                h_temp -= x // n
            else:
                h_temp -= x // n + 1
        
        if h_temp >= 0:
            j = n - 1
            res = n
        elif h_temp < 0:
            i = n + 1

    return res    
        




if __name__ == "__main__":
    piles = [3,6,7,11]
    h = 8
    print(minEatingSpeed(piles, h))
    piles = [30,11,23,4,20]
    h = 5
    print(minEatingSpeed(piles, h))
    piles = [30,11,23,4,20]
    h = 6
    print(minEatingSpeed(piles, h))
    piles = [312884470]
    h = 312884469
    print(minEatingSpeed(piles, h))
