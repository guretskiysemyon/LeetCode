

'''
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Link: https://leetcode.com/problems/search-a-2d-matrix/description/


Solution:
1. Binary search by lines
2. Binary search within the line.

'''

 

def searchMatrix(matrix, target):

    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])

    i = 0
    j = m - 1
    cur = 0

    while i <= j:
        cur = (i + j) // 2
        if matrix[cur][0] <= target <= matrix[cur][n - 1]:
            break
        if matrix[cur][0] > target:
            j = cur - 1
        else:
            i = cur + 1

    i = 0
    j = n - 1
    while i <= j:
        ptr = (i + j) // 2
        if matrix[cur][ptr] == target:
            return True
        elif matrix[cur][ptr] > target:
            j = ptr - 1
        else:
            i = ptr + 1

    return False



if __name__=="__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    searchMatrix(matrix, target)
