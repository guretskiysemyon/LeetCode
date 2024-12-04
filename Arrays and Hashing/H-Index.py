'''
Author: Semyon Guretskiy
'''

'''

274. H-Index
Medium

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least
h papers that have each been cited at least h times.

Link: https://leetcode.com/problems/h-index/description/

Solution:
    Two approaches implemented:
    
    1. Counting Sort Approach:
       - Create count array of citation frequencies
       - Iterate through counts to find h-index
       - Best when citation numbers are small
       
    2. Sorting Approach:
       - Sort citations in ascending order
       - For each citation, check if it qualifies as h-index
       - Simpler implementation but O(n log n)
       
    Time Complexity: 
        Counting Sort: O(n + m) where m is max citation
        Regular Sort: O(n log n)
    Space Complexity:
        Counting Sort: O(m)
        Regular Sort: O(1)
'''

def hIndexCountSort(citations: list[int]) -> int:
    # Find maximum citation for count array size
    maximum = max(citations) if citations else 0
    count = [0] * (maximum + 1)
    
    # Count frequency of each citation number
    for c in citations:
        count[c] += 1
    
    # Find h-index by iterating through counts
    h_index = 0
    acc_papers = 0  # Accumulated papers seen
    n = len(citations)
    
    for i, c in enumerate(count):
        if c == 0:
            continue
        
        # Possible h-index is min of current citation
        # and remaining papers with at least this many citations
        res = min(i, n - acc_papers)
        h_index = max(h_index, res)
        acc_papers += c
    
    return h_index

def hIndexSort(citations: list[int]) -> int:
    # Sort citations in ascending order
    citations.sort()
    
    n = len(citations)
    h_index = 0
    
    # Check each citation as potential h-index
    for i, c in enumerate(citations):
        if c == 0:
            continue
        
        # For current citation, we have n-i papers with at least c citations
        res = min(c, n - i)
        h_index = max(h_index, res)
    
    return h_index

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [3,0,6,1,5],    # Normal case
        [1,3,1],        # Small numbers
        [100],          # Single paper
        [4,4,0,0],      # Multiple same citations
        [0]             # Zero citations
    ]
    
    for citations in test_cases:
        print(f"Citations: {citations}")
        print(f"H-Index: {hIndexSort(citations)}\n")