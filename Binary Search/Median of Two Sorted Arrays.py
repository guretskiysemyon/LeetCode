'''
Author: Semyon Guretskiy
'''

'''
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/


Solution:

'''

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    n = len(nums1)
    m = len(nums2)


    l1 = l2 = 0
    r1 = n - 1
    r2 = m - 1

    while l1 < r1 or l2 < r2:
        m1 = (l1 + r1) // 2
        m2 = (l2 + r2) // 2

        if nums1[m1] == nums2[m2]:
            return nums1[m1]
        
        elif nums1[m1] < nums2[m2]:
            if l1 == r1 or m1 == n - 1:
                r2 = m2 - 1
                l1 = r1
            elif l2 == r2 or m2 == 0:
                l1 = m1 + 1
                r2 = l2
            else:
                l1 = m1 + 1
                r2 = m2 - 1
        else:
            if l1 == r1 or m1 == 0:
                l2 = m2 + 1
                r1 = l1
            elif l2 == r2 or m2 == m - 1:
                r1 = m1 - 1
                l2 = r2
            else:
                r1 = m1 - 1
                l2 = m2 + 1
    
    m1 = (l1+r1) // 2
    m2 = (l2 + r2) // 2
    if (n + m) % 2 == 0:
        return float(nums1[m1] + nums2[m2]) / 2
    
    return min(nums1[m1], nums2[m2])
    
    
        








if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))

    nums1 = [1,2]
    nums2 = [3,4]
    print(findMedianSortedArrays(nums1, nums2))


    numbers = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]
    
    
    for i in range(1,20):
        first = []
        second = []
        for j in range(i):
            first.append(numbers[j])
        
        for k in range(i, 20):
            second.append(numbers[k])
        
        print(findMedianSortedArrays(first, second))
