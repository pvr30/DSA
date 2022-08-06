"""
Given an array A of N elements. Find the majority element in the array.
A majority element in an array A of size N is an element that appears more than N/2 times in the array.
 

Example 1:

Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
Example 2:

Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.


"""
from collections import Counter

def mejorityElement(A, N):
    if len(A) == 1:
        return A[0]
    if (len(set(A)) == len(A)) or len(A) == 2:
        return -1
    print(Counter(A).items())
    for key,value in Counter(A).items():
        if value > N/2:
            return key
    return -1

if __name__ == "__main__":
    print(mejorityElement([3, 1, 3, 3, 2], 5))