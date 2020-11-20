def quickSort_First(A):
    # QuickSort Algorithm

    # Base Case: if length of array A is less than or equal to 1
    # Return A itself as the sorted array, and 0 as number of comparisons happened
    if len(A) <= 1:
        return A,0

    # General Case: divide and conquer
    # using the first element in A as the pivot element 'p'
    # recursively partition array A into two arrays and sort seperately
    # (1st array B containing all elements smaller than pivot and
    # 2nd array C containing all elements larget than pivot)
    # Return the compiled sorted array B+[p]+C, and total count of comparisons happened
    else:
        p = A[0]
        A,Count1,p1 = partition(A)
        B,Count2 = quickSort_First(A[:p1])
        C,Count3 = quickSort_First(A[p1+1:])
        return B+[p]+C , Count1+Count2+Count3

def quickSort_Last(A):
    # QuickSort Algorithm

    # Base Case: if length of array A is less than or equal to 1
    # Return A itself as the sorted array, and 0 as number of comparisons happened
    if len(A) <= 1:
       return A,0

    # General Case: divide and conquer
    # using the last element in A as the pivot element 'p'
    # recursively partition array A into two arrays and sort seperately
    # (1st array B containing all elements smaller than pivot and
    # 2nd array C containing all elements larget than pivot)
    # Return the compiled sorted array B+[p]+C, and total count of comparisons happened
    else:
       p = A[-1]
       A[0],A[-1] = A[-1],A[0]
       A,Count1,p1 = partition(A)
       B,Count2 = quickSort_Last(A[:p1])
       C,Count3 = quickSort_Last(A[p1+1:])
       return B+[p]+C , Count1+Count2+Count3

def quickSort_Middle(A):
    # QuickSort Algorithm

    # Base Case: if length of array A is less than or equal to 1
    # Return A itself as the sorted array, and 0 as number of comparisons happened
    if len(A) <= 1:
       return A,0

    # General Case: divide and conquer
    # using the Middle element as the pivot element 'p'
    # (Refer to README for the definition of the Middle element)
    # recursively partition array A into two arrays and sort seperately
    # (1st array B containing all elements smaller than pivot and
    # 2nd array C containing all elements larget than pivot)
    # Return the compiled sorted array B+[p]+C, and total count of comparisons happened
    else:
        p0 = get_Middle_Index(A)
        p = A[p0]
        A[0],A[p0] = A[p0],A[0]
        A,Count1,p1 = partition(A)
        B,Count2 = quickSort_Middle(A[:p1])
        C,Count3 = quickSort_Middle(A[p1+1:])
        return B+[p]+C , Count1+Count2+Count3

def get_Middle_Index(A):
    # To get the index of the Middle element in array A
    if (A[0]-A[(len(A)-1)//2]) * (A[0]-A[(len(A)-1)]) < 0:
        return 0
    elif (A[(len(A)-1)//2]-A[0]) * (A[(len(A)-1)//2]-A[(len(A)-1)]) < 0:
        return (len(A)-1)//2
    else:
        return len(A)-1

def partition(A):
    # To partition the array A using the first element 'p' as pivot element
    # Return the sorted array, Count of Comparisons happend, and index of 'p' in the sorted array
    Count = 0
    p = A[0]
    l = 0
    r = len(A)
    i = l + 1
    for j in range(l+1,r):
        if A[j] < p:
            A[j],A[i] = A[i],A[j]
            i += 1
        Count += 1
    A[l],A[i-1] = A[i-1],A[l]
    return A,Count,i-1

####Load Data########
# A=[3,8,2,5,1,4,7,6]
# A=[8,3,1,2,5,4,7,6]
A=[]
with open ('QuickSort.txt') as file:
    for line in file:
        A.append(int(line))

import copy

print(quickSort_First(copy.deepcopy(A))[1]) # 162085
print(quickSort_Last(copy.deepcopy(A))[1]) # 164123
print(quickSort_Middle(copy.deepcopy(A))[1]) # 138382
